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


def picaname():
    here = whereami()
    #now, depart, scheduled = whattimeisit()
    if here == "AOC101":
        

        return now, here, 
    csvFile = pd.read_csv("Book1.csv")
    row = timemath.roww()
    out = csvFile.at[row, "name"]
    return out

def whendoileave():
    
    return
def whereami():
    


    return

def whattimeisit():
    


    return