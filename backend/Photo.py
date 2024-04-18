class Image:
    def __init__(self, filename, image):
        self.filename = filename
        self.image = image
        self.hash = None
        self.blur_value = None
        self.similar_photos = set()
    
    def calculate_hash(self):
        self.hash = imagehash.average_hash(self.image)
    
    def calculate_blur_value(self):
        image_cv = cv2.imread(self.filename)
        gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        self.blur_value = laplacian_var
    
    def is_similar(self, other):
        if self.hash is None:
            self.calculate_hash()
        if other.hash is None:
            other.calculate_hash()
        return self.hash - other.hash < 5
    
    def __str__(self):
        return self.filename