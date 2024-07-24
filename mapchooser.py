from re import L
from geopy.geocoders import *
import geocoder
import pandas as pd

def where_am_i():
    g = geocoder.ip('me')
    cords = g.latlng
    lat = cords[0]
    lon = cords[1]
    #lon = -97.144955
    #lat = 33.210455
    return lat, lon
def who_am_i(name_given):
    me = name_given.replace(" ", "_")
    global route_name 
    route_name = me
    return me
def my_name(name):
    global its
    its = name
def whats_my_name():
    return its
def what_direction():
    route_name
    csvFile = pd.read_csv("output.csv")
    directions = csvFile["direction_id"]
    return directions[what_row()]
def pick_a_name():
    csvFile = pd.read_csv("output.csv")
    names = csvFile["route_long_name"]
    return names
def roww(row):
    global roww
    roww = row
def what_row():
    return roww