import mapwithbus
import mapchooser
import apiaccess







lat, lon = mapchooser.where_am_i()
response = apiaccess.nearby_routes(lat, lon)
#print(response)
#apiaccess.nearby_routes(lat, lon)
#print(mapchooser.who_am_i("Centre Place"))
pick_a_name = mapchooser.pick_a_name()                              #set pick_a_name variable to display the schedule set it to return a value 0 to however many there are
row = 4
mapchooser.roww(row)                                                #do that here as the row variable 

name = mapchooser.who_am_i(pick_a_name[mapchooser.what_row()])
mapchooser.my_name(name)
mapwithbus.select_map(name)
mapwithbus.bus_stop_map()