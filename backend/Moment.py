class Moment:
    def __init__(self, id, date, location, photos=set(), title=None, description=None):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.location = location
        self.photos = photos
        self.best_photo = None

    def __str__(self):
        return f"{self.id}: {self.title} ({self.date})"
    
    def add_photo(self, filename):
        '''Add a photo to the moment.'''
        self.photos.add(filename)

    def remove_photo(self, filename):
        '''Remove a photo from the moment.'''
        self.photos.remove(filename)

    def get_best_photo(self, photos_dict):
        '''Return the best photo in the moment.'''
        if self.best_photo:
            return self.best_photo
        else:
            self.set_best_photo(photos_dict)
            return self.best_photo

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "location": self.location,
            "photo": self.photo
        }
    
    def set_best_photo(self, photos_dict):
        photos = [(p.blur_value, p.filename) for p in photos_dict.values() if p.filename in self.photos]
        print(f"photos are ", photos)
        least_blurry = min(photos)[1]
        print(f"least_blurry is ", least_blurry)
        self.best_photo = least_blurry
            

    @staticmethod
    def from_dict(data):
        return Moment(
            data.get("id"),
            data.get("title"),
            data.get("description"),
            data.get("date"),
            data.get("location"),
            data.get("photo")
        )