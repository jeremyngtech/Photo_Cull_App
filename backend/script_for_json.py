import os
import json
import cv2
import imagehash
from PIL import Image as PILImage

def calculate_image_hash(image_path):
    image = PILImage.open(image_path)
    return str(imagehash.average_hash(image))

def calculate_blur_value(image_path):
    image_cv = cv2.imread(image_path)
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

def create_photo_json(filename, image_path):
    return {
        "filename": filename,
        "hash": calculate_image_hash(image_path),
        "blur_value": calculate_blur_value(image_path),
        "similar_photos": []  # This will be empty initially, comparison might be done later
    }


def find_similar_photos(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if int(data[i]["hash"], 16) - int(data[j]["hash"], 16) < 3:
                data[i]["similar_photos"].append(data[j]["filename"])
                data[j]["similar_photos"].append(data[i]["filename"])
    return data

def process_photos(directory):
    photos_json = []
    for filename in os.listdir(directory):
        print("Searching for photos in directory")
        if filename.lower().endswith('.jpg'):
            print(f"Found {filename} in directory")
            photo_info = create_photo_json(filename, os.path.join(directory, filename))
            photos_json.append(photo_info)
    updated_json = find_similar_photos(photos_json)
    return updated_json

# Directory containing the applicable files
jpeg_directory = '../src/lib/jeremy_lib'
json_file_path = '../src/library.JSON'


if __name__ == '__main__':
    choice = input("1. Reset JSON file\n2. Run script to process photos\n3. Exit\nEnter your choice:")
    while choice != '3':
        if choice == '1':
            data = {"Photos": [], "Moments": []}
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
                print("JSON file has been reset.\n")
        elif choice == '2':
            photos_json = process_photos(jpeg_directory)
            data["Photos"].extend(photos_json)
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
        choice = input("1. Reset JSON file\n2. Run script to process photos\n3. Exit\nEnter your choice:")
