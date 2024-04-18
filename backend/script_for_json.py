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

def process_photos(directory):
    photos_json = []
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpeg'):
            photo_info = create_photo_json(filename, os.path.join(directory, filename))
            photos_json.append(photo_info)
    return photos_json

# Directory containing the JPEG files
jpeg_directory = './src/lib/jeremy_lib'

# Process the photos and get the JSON objects
photos_json = process_photos(jpeg_directory)

# Load existing JSON file or create a new one if not exists
json_file_path = './src/library.JSON'
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
else:
    data = {"Photos": [], "Moments": []}

# Add new photos to the JSON data
data["Photos"].extend(photos_json)

# Save the updated JSON data
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)
