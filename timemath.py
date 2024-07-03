import time
import datetime
import shapely.geometry
def timediff(time1, time2):
    
    last_departing_S_stop = "Venue"
    last_departing_S_time = datetime.datetime.strptime(time1, '%H:%M')
    last_departing_R_time = datetime.datetime.strptime(time2, '%H:%M')
    diff = last_departing_R_time - last_departing_S_time


    return diff                 #difference in scheduled departure and real departure

def timepcent(diff):
    time1 = "8:04"              #first inbound time
    time2 = "8:20"              #last inbound time
    time3 = "8:18"              #stop 5 scheduled time

    start = datetime.datetime.strptime(time1, '%H:%M')
    stop = datetime.datetime.strptime(time2, '%H:%M')
    five = datetime.datetime.strptime(time3, '%H:%M')
    inbound = stop - start
    scheduled = five - start
    real = (scheduled)/inbound
    out = round(real, 2)

    print(out)
    return out