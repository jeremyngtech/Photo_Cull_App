"""
This script reads image files from a designated directory and updates a JSON file
to predict how they should be organized in the gallery view of the app.
Photos and Moments are represented as objects and stored in respective dictionaries.
"""
import os
import json
import numpy as np
from PIL import Image
from Photo import Photo
from Moment import Moment
from helpers import convert
from sklearn.cluster import DBSCAN
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
JPEG_DIRECTORY = '../src/lib/jeremy_lib'
JSON_FILE_PATH = '../src/library.JSON'

# Global dictionaries
photos_dict = {}
moments_dict = {}

def find_moments():
    """Cluster photos into moments based on similarity, location, and time."""
    photo_list = list(photos_dict.values())
    photo_features = [prepare_features(photo) for photo in photo_list]
    photo_features = np.array(photo_features)
    clustering = DBSCAN(eps=1, min_samples=2).fit(photo_features)

    print(clustering.labels_)
    for idx, l in enumerate(clustering.labels_):
        label = str(l + 1)
        photo = photo_list[idx]
        logging.info(f"Photo {photo.filename} has label {label}")
        if label not in moments_dict:
            print(f"Creating moment for label {label}")
            moments_dict[label] = Moment(label, photo.timestamp, photo.location)
        print(f"Calling add for {photo.filename} to moment {label}")
        moments_dict[label].add_photo(photo.filename)

def prepare_features(photo):
    """Prepare feature vector for clustering."""
    time_normalized = photo.get_datetime().timestamp() / 120
    hash_normalized = int(photo.hash, 16) / float(2**64)
    location = photo.get_location() if photo.get_location() else (0, 0)
    location_normalized = (location[0] / 45, location[1] / 90)
    return [time_normalized, hash_normalized] + list(location_normalized)

def find_similar_photos():
    """Identify similar photos based on predefined criteria."""
    for photo1 in photos_dict.values():
        for photo2 in photos_dict.values():
            if photo1.filename != photo2.filename and photo1.is_similar(photo2):
                photo1.similar_photos.add(photo2.filename)
                photo2.similar_photos.add(photo1.filename)

def process_photo(filename, photo_path):
    """Process a single photo and load it into the photos dictionary."""
    try:
        img = Image.open(photo_path)
        photo = Photo(filename, photo_path, img)
        photos_dict[filename] = photo
    except IOError:
        logging.error(f"Unable to open {photo_path}")

def process_directory(directory, testing=False):
    """Process all photos in a directory and handle JSON serialization."""
    try:
        for filename in os.listdir(directory):
            if filename.lower().endswith('.jpg'):
                process_photo(filename, os.path.join(directory, filename))
                if testing and len(photos_dict) == 10:
                    break
        find_similar_photos()
        find_moments()
        print("Moments complete")
        return serialize_data()
    except Exception as e:
        logging.error(f"Error processing directory {directory}: {str(e)}")
        return None

def serialize_data():
    """Convert photos and moments dictionaries to JSON serializable format."""
    photos_j = [photo.to_dict() for photo in photos_dict.values()]
    moments_j = [moment.to_dict() for moment in moments_dict.values()]
    return [photos_j, moments_j]

def initialize(directory=JPEG_DIRECTORY, testing=False):
    """Initialize the JSON file with photos and moments from the directory."""
    data = {"Photos": [], "Moments": []}
    lib_json = process_directory(directory, testing)
    print(f"lib json{lib_json}")
    data["Photos"].extend(lib_json[0])
    data["Moments"].extend(lib_json[1])
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4, default=convert)

if __name__ == '__main__':
    choice = input("Choose an action: [1] Reset JSON, [2] Run script, [3] Process first 51 photos, [4] Exit: ")
    actions = {'1': lambda: json.dump({"Photos": [], "Moments": []}, open(JSON_FILE_PATH, 'w'), indent=4),
               '2': lambda: initialize(JPEG_DIRECTORY),
               '3': lambda: initialize(JPEG_DIRECTORY, True),
               '4': lambda: exit()}
    while choice not in actions:
        logging.info("Invalid choice. Please select a valid option.")
        choice = input("Choose an action: [1] Reset JSON, [2] Run script, [3] Process first 10 photos, [4] Exit: ")
    actions[choice]()
