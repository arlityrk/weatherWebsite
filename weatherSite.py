#!/usr/bin/env python3.4
import json
import urllib.request

from bottle import default_app, route, request


@route('/')
def ip():
    ip_api_key = '<key>'
    user_ip = request.remote_addr

    baseipurl = 'http://api.ipinfodb.com/v3/ip-city/'
    url = baseipurl + "?key=" + ip_api_key + "&ip=" + user_ip + "&format=json"
    response = urllib.request.urlopen(url)
    content = response.read()
    data = json.loads(content.decode("UTF8"))
    cityName = (data["cityName"][ : ])

    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityName + ',est'
    weather_response = urllib.request.urlopen(weather_url)
    weather_content = weather_response.read()
    weather_data = json.loads(weather_content.decode("UTF8"))
    main_data = (weather_data["main"])

    #TODO : temp from F to C. Format output
    return "Location: " + cityName + ", Weather data: " + str(main_data)
application = default_app()