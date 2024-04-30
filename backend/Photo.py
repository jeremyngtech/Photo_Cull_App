from helpers import extract_location, calculate_blur_value, get_date_time, similar_location, check_time_difference
from datetime import datetime
import imagehash

class Photo:
    def __init__(self, filename, path, img):
        self.filename = filename
        self.path = path
        self.image = img
        self.hash = str(imagehash.phash(img))
        self.blur_value = calculate_blur_value(path)
        self.similar_photos = set()
        self.location = extract_location(img) # Tuple of latitude and longitude
        self.timestamp = get_date_time(img) # Date and time of the photo
        self.is_selected = False

    def get_location(self, type="tuple"):
        '''Returns location in designated format. Default is tuple.'''
        if self.location == "Not available":
            # Returning not available as None
            # May want to change this to some other default
            return None
        else:
            return self.location
        
    def get_datetime(self):
        """
        Convert the timestamp string to a datetime object.
        """
        try:
            # Assuming the timestamp format is 'YYYY:MM:DD HH:MM:SS'
            return datetime.strptime(self.timestamp, '%Y:%m:%d %H:%M:%S')
        except ValueError as e:
            print(f"Error parsing timestamp for {self.filename}: {str(e)}")
            return None
    
    def is_similar(self, other):
        '''Check if two photos are similar based on hash, location, and time.'''
        within_minutes = 2
        sim_time = check_time_difference(self, other, within_minutes)
        sim_location = similar_location(self, other)
        
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
        hash_diff = imagehash.hex_to_hash(self.hash) - imagehash.hex_to_hash(other.hash)
        if hash_diff < hash_similarity_threshold:
            return True
        return False
    
    def __str__(self):
        return self.filename
    
    def to_dict(self):
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