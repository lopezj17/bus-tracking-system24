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
import apiaccess

def bus_stop_map():
    path = os.getcwd()
    csvFile = pd.read_csv("output.csv")
    lats = csvFile["stop_lat"]
    lons = csvFile["stop_lon"]
    route_name = csvFile["route_long_name"]
    

    fig = go.Figure(go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=12
        ),
        text=route_name
    ))
    

    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=12,
        mapbox_center={"lat": lats.mean(), "lon": lons.mean()},
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )
    #fig.show()
    #fig.write_html(path + "\nearby_stops.html", full_html=True)

def select_map(name):
    path = os.getcwd()
    print(name)
    direction = mapchooser.what_direction()
    if direction == 0:
        writebus1 = True
        writebus2 = False
    if direction == 1:
        writebus1=False
        writebus2=True
    
    my_lat,my_lon = mapchooser.where_am_i()

    path = os.getcwd()
    unt_stops = pd.read_csv(fr"G:\unt\fall2023\Data\Data project\test analysis\all stops\tables\{name}.csv")
    shapefile_path = fr"G:\unt\summer 2024\New folder\all\{name}.shp"
    geo_df = gpd.read_file(shapefile_path)
    lats, lons, names, categories = [], [], [], []
    bus_lats, bus_lons = [], []

    test = 0
    tset = 0
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
            #Outbound bus
            test += 1
            while test == 1:
                if writebus2:
                    inbnd = False
                    otbnd = True
                    lock = timemath.timepcent(timemath.timediff(inbnd, otbnd))
                    if lock < 0:
                        mathlock = (lock - 1) * -1
                        bus = linestring.interpolate(mathlock, normalized=True)
                    bus = linestring.interpolate(lock, normalized=True)
                    bus_lats.append(bus.y)
                    bus_lons.append(bus.x)
                    writebus1 = False
                test +=1
            tset += 1
            while tset == 2:
            #Inbound bus
                if writebus1:
                    inbnd = True
                    otbnd = False
                    lock = timemath.timepcent(timemath.timediff(inbnd, otbnd))
                    if lock > 0:
                        mathlock = (lock - 1) * -1
                        bus1 = linestring.interpolate(mathlock, normalized=True)
                    bus1 = linestring.interpolate(lock, normalized=True)
                    bus_lats.append(bus1.y)
                    bus_lons.append(bus1.x)
                    writebus2 = False
                tset +=1
    fig = go.Figure()
    
    #me
    fig.add_trace(go.Scattermapbox(
        lat = [my_lat],
        lon = [my_lon],
        mode="markers",
        marker=go.scattermapbox.Marker(size=15, color="rgb(25, 150, 300)", opacity=0.9),
        text=["My Location"],
        hoverinfo="text",
        name="My Location"
    ))

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
    #fig.write_html(path + "\map_example.html", full_html=True)

    fig.show()
