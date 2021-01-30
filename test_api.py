import requests
import numpy as np

api_key = 'b602671a12cd092eb876f102ca211cfd'
city = 'Barcelona'

weather_api_call = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key
weather_api_call_tomorrow = 'https://api.openweathermap.org/data/2.5/onecall?lat=41.3851&lon=2.1734&exclude=hourly&appid=' + api_key


response = requests.get(weather_api_call_tomorrow)

day_num = 1

description = response.json()["daily"][day_num]["weather"][0]["description"]

temperature = int(response.json()["daily"][day_num]["temp"]["day"])
temperature = str(np.round(temperature-273,0))

weather_keys = response.json()["daily"][day_num].keys()
raining = bool("rain" in weather_keys)

if raining:
    rain_text = "Tomorrow will rain."
else:
    rain_text = ""

text = "Tomorrow's sky: " + description + ". Tomorrow's day temperature: " + temperature + " ºC. " + rain_text

print(text)