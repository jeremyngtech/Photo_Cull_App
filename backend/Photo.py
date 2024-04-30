from helpers import extract_location, calculate_blur_value, get_date_time, similar_location, check_time_difference
from datetime import datetime
import imagehash
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Photo:
    def __init__(self, filename, path, img):
        self.filename = filename
        self.path = path
        self.image = img
        self.hash = str(imagehash.phash(img))
        self.blur_value = calculate_blur_value(path)
        self.similar_photos = set()
        self.location = extract_location(img)  # Extracted as tuple of latitude and longitude
        self.timestamp = get_date_time(img)  # Date and time of the photo
        self.is_selected = False

    def get_location(self, type="tuple"):
        """
        Return location in the designated format.
        Default is tuple, but can support other formats if implemented.
        """
        if self.location == "Not available":
            logging.info(f"Location not available for {self.filename}")
            return None
        return self.location
        
    def get_datetime(self):
        """
        Convert the timestamp string to a datetime object.
        Handles errors in parsing timestamp format.
        """
        try:
            return datetime.strptime(self.timestamp, '%Y:%m:%d %H:%M:%S')
        except ValueError as e:
            logging.error(f"Error parsing timestamp for {self.filename}: {e}")
            return None
    
    def is_similar(self, other):
        """
        Determine if two photos are similar based on hash, location, and time.
        Adjusts the hash similarity threshold based on location and time proximity.
        """
        sim_time = check_time_difference(self, other, minutes_specified=2)
        sim_location = similar_location(self, other)
        
        if sim_location == 2 and not sim_time:
            hash_similarity_threshold = 15  # Locations not available, different times
        elif sim_location == 1 and not sim_time:
            hash_similarity_threshold = 25  # Same location, different times
        elif sim_location == 2 and sim_time:
            hash_similarity_threshold = 30  # Locations not available, same time
        else:
            hash_similarity_threshold = 42  # Same location, same time

        hash_diff = imagehash.hex_to_hash(self.hash) - imagehash.hex_to_hash(other.hash)
        return hash_diff < hash_similarity_threshold
    
    def __str__(self):
        return self.filename
    
    def to_dict(self):
        """
        Convert the Photo object to a dictionary for easier serialization.
        Converts similar_photos from a set to a list for JSON compatibility.
        """
        return {
            "filename": self.filename,
            "path": self.path,
            "hash": self.hash,
            "blur_value": self.blur_value,
            "similar_photos": list(self.similar_photos),
            "location": self.location,
            "timestamp": self.timestamp,
            "is_selected": self.is_selected
        }
