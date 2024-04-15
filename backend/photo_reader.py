import cv2
import os
import imagehash
from PIL import Image
import numpy as np

def evaluate_photos(directory):
    photo_hashes = {}
    blur_values = {}
    
    # Load and process each photo in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            filepath = os.path.join(directory, filename)
            image = Image.open(filepath)
            
            # Calculate the image's hash for similarity check
            photo_hash = imagehash.average_hash(image)
            photo_hashes[filename] = photo_hash
            
            # Calculate the blurriness of the photo
            image_cv = cv2.imread(filepath)
            gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
            blur_values[filename] = laplacian_var
            
    # Compare each photo with every other photo to find similarities
    similar_photos = {name: set() for name in photo_hashes.keys()}
    for name1, hash1 in photo_hashes.items():
        for name2, hash2 in photo_hashes.items():
            if name1 != name2 and hash1 - hash2 < 5:  # hash difference threshold for similarity
                similar_photos[name1].add(name2)
                similar_photos[name2].add(name1)
    
    return similar_photos, blur_values

# Example usage
directory = 'blog_post'
similar_photos, blur_values = evaluate_photos(directory)
print("Similar photos: ")
for val in similar_photos:
    if len(similar_photos[val]) > 0:
        print(f'{val}: {similar_photos[val]}')

print('- - - - - -')
print("Blurry to least blurry:")
blur_values_pr = [ (v,k) for k,v in blur_values.items() ]
blur_values_pr.sort()
for v,k in blur_values_pr:
    print(f'{k}: {v}')