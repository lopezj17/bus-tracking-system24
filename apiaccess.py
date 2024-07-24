import datetime
import csv
import pandas as pd
import requests
import json
from geopy.geocoders import *
import geocoder
import string

def nearby_routes(lat, lon):
    api_key = 'dabe58733d866f8c661fe595b0e1478fe4de6bf9439782f2c5b47607098bbed5'
    endpoint = 'https://external.transitapp.com/v3/public/nearby_routes'
    params = {
        'lat': lat,
        'lon': lon,
        'max_distance': 200,
        "should_update_realtime" : True
    }
    headers = {
        'apiKey': api_key
    }
    #print("Sending API request for stop departures with parameters:", params)
    response = requests.get(endpoint, params=params, headers=headers)
    #print("Status Code:", response.status_code)
    #print("Response Text:", response.text)
    write_routes(response.text)
def write_routes(response):
    data = json.loads(response)
    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["global_route_id", "direction_headsign","direction_id", "departure_time", "is_cancelled","rt_trip_id","scheduled_departure_time", "trip_search_key", "route_long_name", "stop_lat", "stop_lon"])
        for route_info in data["routes"]:
            global_route_id = route_info['global_route_id']
            route_long_name = route_info["route_long_name"]
            for itinerary in route_info['itineraries']:
                direction_headsign = itinerary['direction_headsign']
                direction_id = itinerary['direction_id']
                merged_headsign = itinerary['merged_headsign']
                closest_stop = itinerary['closest_stop']
                stop_lat = closest_stop['stop_lat']
                stop_lon = closest_stop["stop_lon"]
                for schedule_item in itinerary['schedule_items']:
                    csvwriter.writerow([
                        global_route_id, direction_headsign, direction_id, 
                        schedule_item['departure_time'], 
                        schedule_item['is_cancelled'], 
                        schedule_item['rt_trip_id'], schedule_item['scheduled_departure_time'], 
                        schedule_item['trip_search_key'], route_long_name, stop_lat, stop_lon
                    ])
                    
"""
def nearby_Stops(lat, lon):
    api_key = 'dabe58733d866f8c661fe595b0e1478fe4de6bf9439782f2c5b47607098bbed5'
    endpoint = 'https://external.transitapp.com/v3/public/nearby_stops'
    params = {
        'lat': lat,
        'lon': lon,
        'max_distance': 304
    }
    headers = {
        'apiKey': api_key
    }
    #print("Sending API request for stop departures with parameters:", params)
    response = requests.get(endpoint, params=params, headers=headers)
    #print("Status Code:", response.status_code)
    #print("Response Text:", response.text)
    stop_ids = write_nerby_stops(response.text)
    
    response = stop_departures(stop_ids)
    return response

def write_nerby_stops(response):
    data = json.loads(response)
    global_stop_ids = []
    for stop_info in data["stops"]:
        global_stop_id = stop_info['global_stop_id']
        global_stop_ids.append(global_stop_id)
    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["global_stop_id"])
        for stop_id in global_stop_ids:
            csvwriter.writerow([stop_id])
    #print(global_stop_ids[0])
            
    csvFile = pd.read_csv("output.csv")
    stop_ids = csvFile["global_stop_id"]
    return stop_ids
def stop_departures(stop_ids):
    api_key = 'dabe58733d866f8c661fe595b0e1478fe4de6bf9439782f2c5b47607098bbed5'
    endpoint = 'https://external.transitapp.com/v3/public/stop_departures'
    
    params = {
        'global_stop_id': stop_ids,
        'remove_cancelled': True,
        'should_update_realtime': True
    }
    headers = {'apiKey': api_key}
    #print("Sending API request for stop departures with parameters:", params)
    response = requests.get(endpoint, params=params, headers=headers)
    #print("Status Code:", response.status_code)
    #print("Response Text:", response.text)
    
    write_stop_departures(response.text)
    return 
    


def write_stop_departures(response):
    data = json.loads(response)
    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["global_route_id", "direction_headsign","direction_id", "departure_time", "is_cancelled","rt_trip_id","scheduled_departure_time", "trip_search_key", "route_long_name"])
        for route_info in data["route_departures"]:
            global_route_id = route_info['global_route_id']
            route_long_name = route_info["route_long_name"]
            for itinerary in route_info['itineraries']:
                direction_headsign = itinerary['direction_headsign']
                direction_id = itinerary['direction_id']
                merged_headsign = itinerary['merged_headsign']
                for schedule_item in itinerary['schedule_items']:
                    csvwriter.writerow([
                        global_route_id, direction_headsign, direction_id, 
                        schedule_item['departure_time'], 
                        schedule_item['is_cancelled'], 
                        schedule_item['rt_trip_id'], schedule_item['scheduled_departure_time'], 
                        schedule_item['trip_search_key'], route_long_name
                    ])"""