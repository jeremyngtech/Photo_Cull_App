import cv2
import imagehash
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime, timedelta
import numpy as np

def convert(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj

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


def check_time_difference(photo1, photo2, minutes_specified=4):
    time1 = photo1.get_datetime()
    time2 = photo2.get_datetime()

     # Calculate the difference in time
    time_difference = abs(time1 - time2)
    
    # Check if the difference is less than or equal to the threshold
    return time_difference <= timedelta(minutes=minutes_specified)


def similar_location(photo1, photo2):
    if photo1.location == "Not available" or photo2.location == "Not available":
        return 2
    long1 = float(photo1.location[1])
    long2 = float(photo2.location[1])

    lat1 = float(photo1.location[0])
    lat2 = float(photo2.location[0])

    if abs(lat1 - lat2) < 1 and abs(long1 - long2) < 1:
        return 1
    return 0

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