import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Moment:
    def __init__(self, id, date, location, title=None, description=None):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.location = location
        self.photos = set()
        self.best_photo = None

    def __str__(self):
        title_display = self.title if self.title else "No Title"
        return f"{self.id}: {title_display} ({self.date})"
    
    def add_photo(self, filename):
        """
        Add a photo to the moment.
        Logs the addition and current state of the photos set.
        """
        self.photos.add(filename)
        logging.info(f"Added photo {filename} to moment {self.id}. Photos now: {self.photos}")

    def remove_photo(self, filename):
        """
        Remove a photo from the moment.
        Handles the case where the photo does not exist.
        """
        try:
            self.photos.remove(filename)
            logging.info(f"Removed photo {filename} from moment {self.id}")
        except KeyError:
            logging.error(f"Attempted to remove non-existent photo {filename} from moment {self.id}")

    def get_best_photo(self, photos_dict):
        """
        Return the best photo in the moment, determined by the lowest blurriness value.
        Caches the best photo once calculated.
        """
        if not self.best_photo:
            self.set_best_photo(photos_dict)
        return self.best_photo

    def set_best_photo(self, photos_dict):
        """
        Sets the photo with the lowest blurriness value as the best photo.
        Does nothing if no photos are available.
        """
        try:
            least_blurry = min((photos_dict[p].blur_value, p) for p in self.photos if p in photos_dict)
            self.best_photo = least_blurry[1]
            logging.info(f"Best photo for moment {self.id} is {self.best_photo}")
        except ValueError:
            logging.warning(f"No photos to choose from for moment {self.id}")
            self.best_photo = None

    def to_dict(self):
        """
        Convert the Moment object to a dictionary for easier serialization.
        """
        return {
            "id": self.id,
            "title": self.title or "No Title",
            "description": self.description or "No Description",
            "date": self.date,
            "location": self.location,
            "photos": list(self.photos),
            "best_photo": self.best_photo
        }
