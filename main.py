
import yaml
import io
import datetime
import logging
import sys

import getTime
import hue

#read yaml file and set values
with io.open("conf.yaml","r",encoding="utf8") as file:
    data = yaml.safe_load(file)
    ip = str(data["ip"])
    cords = str(data["cords"])
#set values as lon and lat variables

cords_list = cords.split(",")
lon=float(cords_list[0])
lat=float(cords_list[1])

hue_obj = hue.lights(ip)
turned_on = 0
with open("usage.log", "w") as log:
    try:
        while True:
            #generate sun object (UP/DOWN)
            current_time = datetime.datetime.now()
            sun = getTime.sun_time(lon, lat)
            if current_time > sun.UP.replace(tzinfo=None) and current_time < sun.DOWN.replace(tzinfo=None):
                if hue_obj.getStatus():
                    turned_on += 1
                    log.write("You Tried to turn the light on:  "+str(turned_on)+" times\n")
                    hue_obj.turnOFF()
                pass
    except KeyboardInterrupt:
        sys.exit(0)

