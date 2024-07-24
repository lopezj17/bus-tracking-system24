import time
import datetime
import shapely.geometry
import pandas as pd
import mapchooser

def unix_to_time():
    row = mapchooser.what_row()
    csvFile = pd.read_csv("output.csv")
    depart_time = csvFile["departure_time"]
    sched_time = csvFile["scheduled_departure_time"]
    
    depart = datetime.datetime.fromtimestamp(depart_time[row])
    sched = datetime.datetime.fromtimestamp(sched_time[row])
    fdepart = depart.strftime('%I:%M')
    fsched = sched.strftime('%I:%M')
    return fdepart, fsched
def timediff(inbnd, otbnd):
    row = mapchooser.what_row()
    csvFile = pd.read_csv("output.csv")
    timereal = csvFile["departure_time"]
    timesched = csvFile["scheduled_departure_time"]
    timereal, timesched = unix_to_time()


    last_departing_S_time = datetime.datetime.strptime(timereal, '%H:%M')
    last_departing_R_time = datetime.datetime.strptime(timesched, '%H:%M')
    diff = last_departing_R_time - last_departing_S_time
    if diff.total_seconds() < 0:
        diff = - diff
    #print (diff)
    return diff                 #difference in scheduled departure and real departure
def sched_info():
    row = mapchooser.what_row()
    here = mapchooser.whats_my_name()
    shed = pd.read_csv("Schedule.csv")
    csvFile = pd.read_csv("output.csv")
    zero = 0
    api_depart = csvFile.at[row, "departure_time"]
    times = len(shed)
    x = 0
    name = shed.at[zero,"route_name"]
    end = 0
    inorout = 0
    stopreturn= 0
    while x < times:
        name = shed.at[zero, "route_name"]
        start = shed.at[zero, "start_time"]
        y = 1
        while y < 9:
            stopnumber = "stop_"
            stopnumber = stopnumber + str(y)
            stop = shed.at[zero,stopnumber]
            #
            nextstop = stopnumber + str(y + 1)                                              #NEXT stop 
            #
            if stop == shed.at[zero,"end_time"] and shed.at[zero, "in/outbound"] == "in":   #overflow cases
                nxtstop = "stop_1"
                one = zero + 1
                nextstop = shed.at[one, nxtstop]
            if name == here and stop == api_depart:
                stopreturn = stop
                inorout = shed.at[zero, "in/outbound"]
                start = shed.at[zero,"start_time"]
                end = shed.at[zero,"end_time"]
            y += 1
        zero += 1
        x += 1
    if end == 0:
        return start, "7:30", "in", "7:30"
    return start, end, inorout, stopreturn

def timepcent(diff):
    row = mapchooser.what_row()
    start, end, inorout, stopreturn = sched_info()
    csvFile = pd.read_csv("output.csv")
    #real = csvFile.at[row, "departure_time"]
    real, sched = unix_to_time()
    now = datetime.datetime.now()
    if now.hour > 12:
        hour = str(now.hour - 12)           #current time
    else:
        hour = str(now.hour)
    minute = str(now.minute)
    col = ":"
    currenttime = hour + col + minute
    curTime = datetime.datetime.strptime(currenttime, '%H:%M')
    
    start = datetime.datetime.strptime(start, '%H:%M')
    print(end)
    stop = datetime.datetime.strptime(end, '%H:%M')
    real = datetime.datetime.strptime(real, '%H:%M')
    scheduled_travel_time = stop - start
    time_since_departure = (curTime - real) - diff
    ratio = (time_since_departure)/scheduled_travel_time
    return ratio