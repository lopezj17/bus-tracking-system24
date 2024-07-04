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


path = os.getcwd()
print("Current Directory", path)


#Stuff I need to connect later
test = 0
writebus1 = False
writebus2 = True




name = mapchooser.picaname()
unt_stops = pd.read_csv(fr"G:\unt\fall2023\Data\Data project\test analysis\all stops\tables\{name}.csv")
shapefile_path = fr"G:\unt\summer 2024\New folder\all\{name}.shp"
geo_df = gpd.read_file(shapefile_path)


lats, lons, names, categories = [], [], [], []
bus_lats, bus_lons = [], []

for feature, name, category in zip(geo_df.geometry, geo_df["name"] if "name" in geo_df.columns else [""]*len(geo_df), geo_df["route_type"]):
    if isinstance(feature, shapely.geometry.linestring.LineString):
        linestrings = [feature]
    elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString):
        linestrings = feature.geoms
    
    for linestring in linestrings:
        x, y = linestring.xy
        lats.extend(y.tolist() + [None]) 
        lons.extend(x.tolist() + [None])
        names.extend([name] * (len(y) + 1))
        categories.extend([category] * (len(y) + 1))
        


        #Bus lock
        #Get this from excel and api
        
        #Outbound
        while test == 0:
            timereal = "08:18"
            timesched = "08:19"
            lock = timemath.timepcent(timemath.timediff(timereal, timesched))
            bus = linestring.interpolate(lock, normalized=True)
            if writebus1 == True:
                bus_lats.append(bus.y)
                bus_lons.append(bus.x)
            test = 1
        #Inbound
        while  test == 1:
            lock = timemath.timepcent(timemath.timediff(timereal, timesched))
            print(lock)
            mathlock = (lock - 1) * -1
            bus = linestring.interpolate(mathlock, normalized=True)
            if writebus2 == True:
                bus_lats.append(bus.y)
                bus_lons.append(bus.x)
            test = 3





fig = go.Figure()

#Bus routes
fig.add_trace(go.Scattermapbox(
    lat=lats,
    lon=lons,
    mode="lines",
    line=dict(width=4),
    text=names,
    hoverinfo="text",
    name="Routes"
))

#Bus stops
fig.add_trace(go.Scattermapbox(
    lat=unt_stops["stop_lat"],
    lon=unt_stops["stop_lon"],
    mode="markers",
    marker=go.scattermapbox.Marker(size=9, color="rgb(255, 0, 0)", opacity=0.7),
    text=unt_stops["stop_name"],
    hoverinfo="text",
    name="Bus Stops"
))

#Busses
fig.add_trace(go.Scattermapbox(
    lat=bus_lats,
    lon=bus_lons,
    mode="markers",
    marker=go.scattermapbox.Marker(size=15, color="rgb(0, 255, 0)", opacity=0.9),
    text=["Bus on Route"]*len(bus_lats),
    hoverinfo="text",
    name="Buses"
))


fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=12,
    mapbox_center={"lat": 33.2, "lon": -97.1},
    margin={"r": 0, "t": 0, "l": 0, "b": 0}
)


fig.show()
