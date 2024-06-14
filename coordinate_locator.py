# Get the location of different bus stops
from geopy.geocoders import *
import geocoder

# List of desired stops
bus_stops = ['Morse Transfer, Denton, TX 76208', 'EB Hickory @ Wood, Denton, TX 76205']
coordindate_tracker = []

def get_long_lat(stop_location):
    geolocator = Nominatim(user_agent="my_test_application")
    location = geolocator.geocode(stop_location)
    return (location.latitude, location.longitude)

# Get coordinates for each of the desired bus stops
def get_coordinates(bus_stops):
    global coordindate_tracker
    start_position = bus_stops[0]
    end_position = bus_stops[-1]
    print(start_position)
    start_coord = get_long_lat(start_position)
    print(start_coord)
    print(end_position)
    end_coord = get_long_lat(end_position)

    # Add coordinates to the tracker
    coordindate_tracker.append(start_coord)
    coordindate_tracker.append(end_coord)

    print(coordindate_tracker)

def get_user_location():
    current_location = geocoder.ip('me')
    print(current_location)
    return current_location

get_user_location()
#get_long_lat()