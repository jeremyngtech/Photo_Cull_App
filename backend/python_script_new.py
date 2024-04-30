"""
This script will read image files from the designated directory
and ultimately update the JSON file to predict how they should
be organized in the gallery view of the app. Photos and Moments
are represented as objects in the backend and stored in respective
dictionaries.
"""
import os
import json
import numpy as np
from PIL import Image
from Photo import Photo
from Moment import Moment
from sklearn.cluster import DBSCAN

# Directory containing the applicable files
jpeg_directory = '../src/lib/jeremy_lib'
json_file_path = '../src/library.JSON'

# Initialize the dictionary of photos
photos_dict = {}
moments_dict = {}

def find_moments():
    '''
    Finds moments from the photos_dict and updates moments_dict.
    Uses DBSCAN to cluster photos based on similarity, location, and time.
    '''
    # Create a list of features for clustering
    photo_features = []
    photo_list = list(photos_dict.values())

    for photo in photo_list:
        # Convert timestamp to UNIX time (seconds since epoch)
        time_normalized = photo.get_datetime().timestamp() / 120  # Normalize time by 2 minutes (120 seconds)

        # Convert hash to a suitable form for clustering, assuming hash is already computed
        hash_int = int(str(photo.image_hash), 16)
        # Normalize hash to be between 0 and 1
        hash_normalized = hash_int / float(2**64)

        # Assume get_location returns (lat, lon), normalize these if needed
        location = photo.get_location() if photo.get_location() else (0, 0)  # Default to (0,0) if no location
        location_normalized = (location[0] / 90, location[1] / 180)

        photo_features.append([time_normalized, hash_normalized] + list(location_normalized))

    # Convert list to numpy array for DBSCAN
    photo_features = np.array(photo_features)

     # Apply DBSCAN
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(photo_features)

    # Create Moments based on clusters
    for idx, label in enumerate(clustering.labels_):
        if label not in moments_dict:
            moments_dict[label] = Moment(label)
        moments_dict[label].add_photo(photo_list[idx])
    
    print(moments_dict)


def find_similar_photos():
    '''
    Compares all photos in photos_dict to find similar photos.
    Updates similar_photos attribute of each photo object.
    '''
    for filename1, photo1 in photos_dict.items():
        for filename2, photo2 in photos_dict.items():
            if filename1 != filename2 and photo1.is_similar(photo2):
                photo1.similar_photos.add(filename2)
                photo2.similar_photos.add(filename1)


def process_photo(filename, photo_path):
    '''
    Given a path to a photo, returns a JSON object for that photo.
    Loads corresponding Python Photo object into photos_dict.
    '''
    img = Image.open(photo_path)
    photo = Photo(filename, photo_path, img)
    photos_dict[filename] = photo


def process_directory(directory, test=False):
    '''
    Given a path to a directory, returns a JSON that enables easier manipulation
    of the photos. When testing enabled, will only process a few files.
    '''
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            process_photo(filename, os.path.join(directory, filename))
            if test and len(photos_dict) == 10:
                break
        find_similar_photos()

    # Find moments from photos_dict
    find_moments() 
    
    # Convert all objects in photos dictionary to JSON
    photos_j = []
    for p in photos_dict.values():
        photos_j.append({
            "filename": p.filename,
            "path": p.path,
            "hash": p.hash,
            "blur_value": p.blur_value,
            "location": p.location,
            "timestamp": p.timestamp,
            "is_selected": p.is_selected,
            "similar_photos": list(p.similar_photos)
        })
    # Convert all objects in moments dictionary to JSON\
    moments_j = []
    for m in moments_dict.values():
        moments_j.append({
            "id": m.id,
            "location": m.location,
            "earliest_time": m.earliest_time,
            "photos": list(m.photos),
            "best_photos": list(m.best_photos)
        })
    # Return as one JSON
    return [photos_j, moments_j]



if __name__ == '__main__':
    '''
    Runnable in terminal for testing purposes.
    '''
    choice = input("1. Reset JSON file\n2. Run script to process photos\n3. Run on only first 51 photos\n4. Exit\nEnter your choice:")
    while True:
        data = {"Photos": [], "Moments": []}
        if choice == '1':
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
                print("JSON file has been reset.\n")
        elif choice == '2' or choice == '3':
            lib_json = process_directory(jpeg_directory, choice == '3')
            data["Photos"].extend(lib_json[0])
            data["Moments"].extend(lib_json[1])
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
        elif choice == '4':
            break
        choice = input("1. Reset JSON file\n2. Run script to process photos\n3. Run on only first 51 photos\n4. Exit\nEnter your choice:")