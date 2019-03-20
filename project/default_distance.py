import json
import requests
from info_parser import Info

def default_distance():
    app = Info()
    app.get_personal_info()
    url_format = 'https://www.distance24.org/route.json?stops={}|{}'
    fr = app.city
    to = 'moscow'
    req = requests.get(url_format.format(fr, to))
    x = req.json()
    distance = x['distance']
    return distance

def travel_time(distance):
    travel_speed = 800
    return distance / travel_speed
