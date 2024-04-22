from helpers import get_location, calculate_blur_value, get_date_time, calculate_image_hash

class Photo:
    def __init__(self, filename, path, img):
        self.filename = filename
        self.path = path
        self.image = img
        self.hash = calculate_image_hash(img)
        self.blur_value = calculate_blur_value(path)
        self.similar_photos = set()
        self.location = get_location(img)
        self.time = get_date_time(img)
    
    def is_similar(self, other):
        if self.hash is None:
            self.calculate_hash()
        if other.hash is None:
            other.calculate_hash()
        return self.hash - other.hash < 3
    
    def __str__(self):
        return self.filename