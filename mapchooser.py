import csv
import plotly.graph_objects as go
import pandas as pd
import geopandas as gpd
import shapely.geometry
import numpy as np
import os
import time
import datetime
import timemath
import mapchooser
import string

def picaname():
    row = timemath.roww()
    csvFile = pd.read_csv("Book1.csv")
    here = csvFile.at[row, "name"]
    return here

def schedinfo():
    row = timemath.roww()
    shed = pd.read_csv("Schedule.csv")
    csvFile = pd.read_csv("Book1.csv")
    here = picaname()
    zero = 0
    api_stoptime = csvFile.at[row, "stop"]

    times = len(shed)
    x = 0
    name = shed.at[zero,"route_name"]
    
    while x < times:
        name = shed.at[zero, "route_name"]
        start = shed.at[zero, "start_time"]
        y = 1
        while y < 9:
            stopnumber = "stop_"
            stopnumber = stopnumber + str(y)
            stop = shed.at[zero,stopnumber]
            if name == here and stop == api_stoptime:
                stopreturn = stop
                inorout = shed.at[zero, "in/outbound"]
                start = shed.at[zero,"start_time"]
                stop = shed.at[zero,"stop_time"]
            y += 1
        zero += 1
        x += 1
    return start, stop, inorout, stopreturn


    
def whereami():
    


    return

def whattimeisit():
    


    return