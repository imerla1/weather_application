import requests
import json
from info_parser import Info

def default_temp():
    obj = Info()
    obj.get_personal_info()
    url_base = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    APIKEY = '3fcb9950908ddd9b5672e2a29e4842a2'
    city_name = obj.city
    req = requests.get(url_base.format(city_name, APIKEY))
    default_x = req.json()
    temp =  round(default_x['main']['temp'] - 273.15, 2)
    return temp
    
