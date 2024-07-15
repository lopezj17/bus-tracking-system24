import time
import datetime
import shapely.geometry
import pandas as pd


def roww():
    row = 0               #change the test csv file row
    return row


def times(inbound, outbound):
    row = roww()
    csvFile = pd.read_csv("Book1.csv")
    
    real_stop_departure_time = csvFile.at[row,"real"]
    scheduled_stop_departure_time = csvFile.at[row,"stop"]
    



    inbound_start_time =csvFile.at[row,"start"]
    inbound_end_time=csvFile.at[row,"end"]
    outbound_start_time =csvFile.at[row,"start"]
    outbound_end_time=csvFile.at[row,"end"]

    
    if inbound == True:
        return real_stop_departure_time, scheduled_stop_departure_time, inbound_start_time, inbound_end_time
    if outbound == True:
        return real_stop_departure_time, scheduled_stop_departure_time, outbound_start_time, outbound_end_time

    return
def timediff(inbnd, otbnd):
    timereal, timesched, notn, needed = times(inbnd, otbnd)
    #last_departing_S_stop = stop_name
    last_departing_S_time = datetime.datetime.strptime(timereal, '%H:%M')
    last_departing_R_time = datetime.datetime.strptime(timesched, '%H:%M')
    diff = last_departing_R_time - last_departing_S_time
    if diff.total_seconds() < 0:
        diff = - diff
    print (diff)
    return diff                 #difference in scheduled departure and real departure

def timepcent(diff):
    inbnd = True
    otbnd = True
    notneeded, time3, time1, time2 = times(inbnd, otbnd)
    ##
    now = datetime.datetime.now()
    if now.hour > 12:
        hour = str(now.hour - 12)           #current time
    else:
        hour = str(now.hour)
    minute = str(now.minute)
    col = ":"
    currenttime = hour + col + minute
    #currenttime = "8:15"                    #manual time change 
    curTime = datetime.datetime.strptime(currenttime, '%H:%M')
    ###
    start = datetime.datetime.strptime(time1, '%H:%M')
    stop = datetime.datetime.strptime(time2, '%H:%M')
    real = datetime.datetime.strptime(time3, '%H:%M')
    scheduled_travel_time = stop - start
    time_since_departure = (curTime - real) - diff
    ratio = (time_since_departure)/scheduled_travel_time
    #out = round(real, 2)
    #ratio = .88                              #manual checker
    #print(curTime,start,stop,real,scheduled_travel_time,time_since_departure,)
    return ratio

def timetest():
    csvFile = pd.read_csv("fakeapi.csv")
    test = 0
    while test < 6:
        sched = csvFile.at[test, "scheduled_departure_time"]
        real = csvFile.at[test, "departure_time"]
        inout = csvFile.at[test, "direction_id"]
        if test == 0:
            date_time = datetime.datetime.fromtimestamp(sched)
        test = test + 1
    formatted_time = date_time.strftime('%I:%M')
    print(formatted_time)
    return formatted_time
