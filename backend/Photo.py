from helpers import get_location, calculate_blur_value, get_date_time, calculate_image_hash
from datetime import datetime, timedelta

class Photo:
    def __init__(self, filename, path, img):
        self.filename = filename
        self.path = path
        self.image = img
        self.hash = calculate_image_hash(img)
        self.blur_value = calculate_blur_value(path)
        self.similar_photos = set()
        self.location = get_location(img) # Tuple of latitude and longitude
        self.timestamp = get_date_time(img) # Date and time of the photo
        self.is_selected = False

    def get_location(self, type="tuple"):
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

    def calculate_hash(self):
        self.hash = calculate_image_hash(self.image)
    
    def is_similar(self, other):
        if self.hash is None:
            self.calculate_hash()
        if other.hash is None:
            other.calculate_hash()
        return self.hash - other.hash < 3
    
    def __str__(self):
        return self.filename