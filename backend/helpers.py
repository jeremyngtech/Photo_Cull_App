import cv2
import imagehash
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime, timedelta

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                
def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")
    
    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")
            
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]
    
    return geotagging

def get_decimal_from_dms(dms, ref):
    #Convert dms (an IFDRational object) to a subcriptable object
    #print(f"DMs is {dms}")
    dms = [float(dms[0]), float(dms[1]), float(dms[2])]


    degrees = dms[0]
    minutes = dms[1] / 60.0 
    seconds = dms[2] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return degrees + minutes + seconds


def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
    
    return (lat, lon)

def get_location(img):
    try:
        exif = img._getexif()
        geotags = get_geotagging(exif)
        coordinates = get_coordinates(geotags)
    except (AttributeError, ValueError, KeyError):
        coordinates = "Not available"
    return coordinates

def convert_to_datetime(time_str):
    return datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')

def get_date_time(img):
    exif_data = img._getexif()
    
    # The date and time tag in EXIF data is 36867
    date_time_original = exif_data.get(36867)
    #print(f"Date and time for is {date_time_original}")
    
    return date_time_original

def calculate_image_hash(img):
    return str(imagehash.phash(img))

def calculate_blur_value(image_path):
    image_cv = cv2.imread(image_path)
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var