import cv2
import numpy as np
from PIL import Image, ExifTags
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert(obj):
    """ Convert numpy data types to Python native data types for JSON serialization. """
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj

def extract_exif_data(img):
    """ Extract EXIF data from an image. """
    try:
        return img._getexif()
    except AttributeError as e:
        logging.error("Failed to extract EXIF data: %s", e)
        return None

def get_geotagging(exif):
    """ Retrieve geolocation data from EXIF tags. """
    if not exif:
        logging.error("No EXIF metadata found.")
        return None
    geotagging = {}
    try:
        for (idx, tag) in ExifTags.TAGS.items():
            if tag == 'GPSInfo':
                if idx in exif:
                    for (key, val) in ExifTags.GPSTAGS.items():
                        if key in exif[idx]:
                            geotagging[val] = exif[idx][key]
        return geotagging
    except KeyError as e:
        logging.error("KeyError in getting geotagging: %s", e)
        return None

def get_decimal_from_dms(dms, ref):
    """ Convert degrees, minutes, seconds to decimal format for latitude and longitude. """
    degrees, minutes, seconds = dms
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def get_coordinates(geotags):
    """ Convert geotags to latitude and longitude coordinates. """
    if 'GPSLatitude' in geotags and 'GPSLongitude' in geotags:
        lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
        lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
        return (lat, lon)
    logging.error("Geotags missing GPSLatitude or GPSLongitude.")
    return None

def check_time_difference(photo1, photo2, minutes_specified=4):
    """ Check if two photos were taken within a specified number of minutes of each other. """
    time1 = photo1.get_datetime()
    time2 = photo2.get_datetime()
    if time1 and time2:
        return abs(time1 - time2) <= timedelta(minutes=minutes_specified)
    return False

def similar_location(photo1, photo2):
    """ Determine if two photos were taken at similar geographic locations. """
    if 'Not available' in [photo1.location, photo2.location]:
        return 2
    lat1, long1 = photo1.location
    lat2, long2 = photo2.location
    return int(abs(lat1 - lat2) < 1 and abs(long1 - long2) < 1)

def get_date_time(img):
    """ Extract date and time from an image. """
    exif = extract_exif_data(img)
    if exif:
        for tag, value in exif.items():
            if ExifTags.TAGS.get(tag) == 'DateTimeOriginal':
                return value
    return None

def extract_location(img):
    """ Extract geographical location from an image. """
    exif = extract_exif_data(img)
    if exif:
        geotags = get_geotagging(exif)
        if geotags:
            return get_coordinates(geotags)
    return "Not available"

def calculate_blur_value(image_path):
    """ Calculate the blurriness value of an image using the Laplacian method. """
    image_cv = cv2.imread(image_path)
    if image_cv is not None:
        gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        return cv2.Laplacian(gray, cv2.CV_64F).var()
    logging.error("Failed to load image at %s for blur calculation.", image_path)
    return None