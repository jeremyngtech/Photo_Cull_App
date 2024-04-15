class Moment:
    def __init__(self, id, title, description, date, location, photo):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.location = location
        self.photo = photo

    def __str__(self):
        return f"{self.id}: {self.title} ({self.date})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "location": self.location,
            "photo": self.photo
        }

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