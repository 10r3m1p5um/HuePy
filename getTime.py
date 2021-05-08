from suntime import Sun, SunTimeException
from datetime import date
from dateutil import tz
import pytz
from tzwhere import tzwhere

class sun_time():
    lon = 0
    lat = 0
    UP=""
    DOWN=""

    sun = ""
    to_tz = ""

    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat
        self.main_time()
        self.UP=self.getUP()
        self.DOWN=self.getDOWN()
    
    def main_time(self):
        global sun, to_tz
        tz_where = tzwhere.tzwhere()
        timezone_str = tz_where.tzNameAt(self.lon,self.lat)
        to_tz = tz.gettz(timezone_str)
        sun = Sun(self.lon, self.lat)
    
    def getUP(self):
        return sun.get_sunrise_time().astimezone(to_tz)
    
    def getDOWN(self):
        return sun.get_sunset_time().astimezone(to_tz)
