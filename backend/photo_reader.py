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
from sklearn.neighbors import NearestNeighbors
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
JPEG_DIRECTORY = '../src/lib/jeremy_lib'
JSON_FILE_PATH = '../src/library.JSON'
TEST_THRESHOLD = 20

# Global dictionaries
photos_dict = {}
moments_dict = {}

def choose_eps(features, k=2):
    """Determine an optimal DBSCAN 'eps' value using the k-nearest neighbors method."""
    # Fit NearestNeighbors model to data
    neighbors = NearestNeighbors(n_neighbors=k)
    neighbors.fit(features)
    distances, indices = neighbors.kneighbors(features)

    # Sort and plot the k-th distances
    kth_distances = distances[:, k-1]  # k-1 because index starts at 0
    kth_distances.sort()

    optimal_eps = kth_distances[int(len(kth_distances) * 0.95)]
    print(f"Suggested eps: {optimal_eps}")
    
    return optimal_eps

def find_moments():
    """Cluster photos into moments, adjusting parameters and re-clustering outliers."""
    photo_list = list(photos_dict.values())
    photo_features = np.array([prepare_features(photo) for photo in photo_list])
    
    # First round of clustering
    clustering = DBSCAN(eps=1, min_samples=1).fit(photo_features)
    labels = clustering.labels_
    
    # Identify outliers
    outliers = [i for i, label in enumerate(labels) if label == -1]
    if outliers:
        outlier_photos = [photo_list[i] for i in outliers]

        # Prepare features for outliers without considering location
        outlier_features = np.array([prepare_features(photo, use_location=False) for photo in outlier_photos])
        
        # Second round of clustering just for outliers
        outlier_clustering = DBSCAN(eps=choose_eps(outlier_features), min_samples=1).fit(outlier_features)
        
        # Map new cluster labels to continue after max label from first clustering
        max_label = max(labels)
        new_labels = [label + max_label + 1 if label != -1 else -1 for label in outlier_clustering.labels_]
        
        # Update the original labels array with new labels for outliers
        for index, new_label in zip(outliers, new_labels):
            labels[index] = new_label

    # Process final clustering results
    for label, photo in zip(labels, photo_list):
        if label not in moments_dict:
            moments_dict[label] = Moment(label, photo.timestamp, photo.location if label != -1 else None)
        moments_dict[label].add_photo(photo.filename)
    
    # Set best photo after all moments established
    for moment in moments_dict.values():
        moment.set_best_photo(photos_dict)
            

def prepare_features(photo, use_location=True):
    """Prepare feature vector for clustering with optional location usage."""
    if use_location:
        time_normalized = photo.get_datetime().timestamp() / 120
        hash_normalized = int(photo.hash, 16) / float(2**64) 
        location = photo.get_location()
        if not location:
            location_normalized = (1000, 1000)
        else:
            location_normalized = (location[0] / 45, location[1] / 90)
        return [time_normalized, hash_normalized] + list(location_normalized)
    else:
        time_normalized = photo.get_datetime().timestamp() / 300
        hash_normalized = int(photo.hash, 16) / float(2**64)
        return [time_normalized, hash_normalized]


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
                if testing and len(photos_dict) == TEST_THRESHOLD:
                    break
        find_similar_photos()
        find_moments()
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
    choice = input(f"Choose an action: [1] Reset JSON, [2] Run script, [3] Process first {TEST_THRESHOLD} photos, [4] Exit: ")
    actions = {'1': lambda: json.dump({"Photos": [], "Moments": []}, open(JSON_FILE_PATH, 'w'), indent=4),
               '2': lambda: initialize(JPEG_DIRECTORY),
               '3': lambda: initialize(JPEG_DIRECTORY, True),
               '4': lambda: exit()}
    while choice:
        if choice not in actions:
            logging.info("Invalid choice. Please select a valid option.")
        else:
            actions[choice]()
        choice = input(f"Choose an action: [1] Reset JSON, [2] Run script, [3] Process first {TEST_THRESHOLD} photos, [4] Exit: ")
