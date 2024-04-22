import os
import json
import imagehash
from Photo import Photo
from Moment import Moment
from PIL import Image
from helpers import get_location, convert_to_datetime
from datetime import timedelta

photos_dict = {}
Moments_dict = {}

def add_location_to_json(photos_json):
    for photo in photos_json:
        img = Image.open(photo["path"])
        coordinates = get_location(img)
        photo["location"] = coordinates
    
    return photos_json


def check_time_difference(time_str1, time_str2, minutes_specified=4):
    time1 = convert_to_datetime(time_str1)
    time2 = convert_to_datetime(time_str2)
    
    # Calculate the difference in time
    time_difference = abs(time1 - time2)
    
    # Check if the difference is less than or equal to the threshold
    return time_difference <= timedelta(minutes=minutes_specified)


def create_photo_json(filename, image_path):
    img = Image.open(image_path)
    photo = Photo(filename, image_path, img)
    photos_dict[filename] = photo
    return {
        "filename": filename,
        "path": image_path,
        "hash": photo.hash,
        "blur_value": photo.blur_value,
        "date_time": photo.time,
        "location": photo.location,
        "similar_photos": []  # This will be empty initially, comparison might be done later
    }

def similar_location(i, j, json):
    if json[i]["location"] == "Not available" or json[j]["location"] == "Not available":
        return 2
    long1 = float(json[i]["location"][1])
    long2 = float(json[j]["location"][1])

    lat1 = float(json[i]["location"][0])
    lat2 = float(json[j]["location"][0])

    if abs(lat1 - lat2) < 1 and abs(long1 - long2) < 1:
        return 1
    return 0


def find_similar_photos(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            within_minutes = 2
            sim_time = check_time_difference(data[i]["date_time"], data[j]["date_time"], within_minutes)
            sim_location = similar_location(i, j, data)

            # Locations not available, diff times
            if sim_location == 2 and not sim_time:
                hash_similarity_threshold = 15

            # Same location, diff times
            elif sim_location == 1 and not sim_time:
                hash_similarity_threshold = 25

            # Locations not available, same time
            elif sim_location == 2 and sim_time:
                hash_similarity_threshold = 30
            
            # Same location, same time
            else:
                hash_similarity_threshold = 42

            print(f"Threshold is {hash_similarity_threshold}")    
            hash_diff = imagehash.hex_to_hash(data[i]["hash"]) - imagehash.hex_to_hash(data[j]["hash"])
            if hash_diff < hash_similarity_threshold:
                data[i]["similar_photos"].append(data[j]["filename"])
                data[j]["similar_photos"].append(data[i]["filename"])
                photos_dict[data[i]["filename"]].similar_photos.add(data[j]["filename"])
                photos_dict[data[j]["filename"]].similar_photos.add(data[i]["filename"])
    return data

def find_moments():
    moments_json_builder = []
    moments_dict = {}
    for photo in photos_dict.values():
        # Should belong to a moment
        for moment in moments_dict.values():
            print(f"Moment photos are {moment.photos} and similar photos are {photo.similar_photos}")
            # Set of photos in the moment, by name, will be converted to list later
            for p in photo.similar_photos:
                if p in moment.photos:
                    moment.photos.union(photo.similar_photos)
                    break
        moments_dict[photo.time] = Moment(photo.hash, photo.time, photo.location, photos=photo.similar_photos)
                        
            # else:
            #     moments_dict[photo.time] = Moment(photo.hash, photo.time, photo.location, photos=photo.similar_photos)
        # else:
        #     moments_dict[photo.time] = Moment(photo.hash, photo.time, photo.location, photos={photo.filename})

    for moment in moments_dict.values():
        moments_json_builder.append({
            "id": moment.id,
            "location": moment.location,
            "earliest_time": moment.date,
            "photos": list(moment.photos),
        })
    return moments_json_builder

def process_photos(directory, test=False):
    photos_json = []
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            print(f"Found {filename} in directory")
            photo_info = create_photo_json(filename, os.path.join(directory, filename))
            photos_json.append(photo_info)
            if test and len(photos_json) == 10:
                break
    updated_json = find_similar_photos(photos_json)
    return updated_json

# Directory containing the applicable files
jpeg_directory = '../src/lib/jeremy_lib'
json_file_path = '../src/library.JSON'


if __name__ == '__main__':
    choice = input("1. Reset JSON file\n2. Run script to process photos\n3. Run on only first 51 photos\n4. Exit\nEnter your choice:")
    while True:
        data = {"Photos": [], "Moments": []}
        if choice == '1':
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
                print("JSON file has been reset.\n")
        elif choice == '2' or choice == '3':
            photos_json = process_photos(jpeg_directory, choice == '3')
            data["Photos"].extend(photos_json)
            data["Moments"].extend(find_moments())
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
        elif choice == '4':
            break
        choice = input("1. Reset JSON file\n2. Run script to process photos\n3. Run on only first 51 photos\n4. Exit\nEnter your choice:")