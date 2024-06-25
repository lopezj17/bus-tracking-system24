import plotly.express as px
import pandas as pd

import os
 
# get current directory
path = os.getcwd()
print("Current Directory", path)

unt_stops = pd.read_csv(r"C:\\Users\\lopez\\Downloads\\unt_bus-stops.csv")

fig = px.scatter_mapbox(

    unt_stops,
    lat="stop_lat",
    lon="stop_lon",
    hover_name="stop_name",
    hover_data=["stop_name", "stop_id"],
    color_discrete_sequence=["green"],
    zoom=12,
    height=1000,
    width=1000,

)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(mapbox_bounds={"west": -118, "east": -76, "south": 32.7, "north": 33.4})
#fig.show()
fig.write_html(path + "\\templates\\map_block.html", full_html=True)
