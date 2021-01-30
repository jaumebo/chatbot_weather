# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from random import sample
from typing import Any, Dict, List, Text

import numpy as np
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

api_key = 'b602671a12cd092eb876f102ca211cfd'
city = 'Barcelona'

weather_api_call = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key
weather_api_call_tomorrow = 'https://api.openweathermap.org/data/2.5/onecall?lat=41.3851&lon=2.1734&exclude=hourly&appid=' + api_key

class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        phrases = ["Greetings! What can I do for you today?",
                    "Good to read you again! What can I do for you?",
                    "Hello, what can I do for you today?",
                    "Hey! What can I do for you?"]

        text = sample(phrases,1)[0]

        dispatcher.utter_message(text=text)

        return []

class ActionCurrentWeather(Action):

    def name(self) -> Text:
        return "action_current_weather"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call)

        description = response.json()["weather"][0]["description"]

        temperature = int(response.json()["main"]["temp"])
        temperature = str(np.round(temperature-273,0))

        weather_keys = response.json().keys()
        raining = bool("rain" in weather_keys)

        if raining:
            rain_text = "It is currently raining."
        else:
            rain_text = ""

        text = "Current sky: " + description + ". Current temperature: " + temperature + " ºC. " + rain_text

        dispatcher.utter_message(text=text)

        return []

class ActionCurrentTemperature(Action):

    def name(self) -> Text:
        return "action_current_temperature"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call)

        temperature = int(response.json()["main"]["temp"])
        temperature = str(np.round(temperature-273,0))

        text = "Today's current temperature is " + temperature + "ºC"

        dispatcher.utter_message(text=text)

        return []

class ActionCurrentHumidity(Action):

    def name(self) -> Text:
        return "action_current_humidity"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call)

        humidity = str(response.json()["main"]["humidity"])

        text = "Today's current humidity is " + humidity + "%"

        dispatcher.utter_message(text=text)

        return []

class ActionCurrentRain(Action):

    def name(self) -> Text:
        return "action_current_rain"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call)


        weather_keys = response.json().keys()
        raining = bool("rain" in weather_keys)

        if raining:
            text = "It is currently raining, you should take an umbrella with you!"
        else:
            text = "Currently it is not raining."

        dispatcher.utter_message(text=text)

        return []

class ActionMaximumTemperature(Action):

    def name(self) -> Text:
        return "action_maximum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call)

        temperature = int(response.json()["main"]["temp_max"])
        temperature = str(np.round(temperature-273,0))

        text = "Today's maximum temperature will be " + temperature + "ºC"

        dispatcher.utter_message(text=text)

        return []

class ActionMinimumTemperature(Action):

    def name(self) -> Text:
        return "action_minimum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call)

        temperature = int(response.json()["main"]["temp_min"])
        temperature = str(np.round(temperature-273,0))

        text = "Today's minimum temperature will be " + temperature + "ºC"

        dispatcher.utter_message(text=text)

        return []

class ActionTomorrowWeather(Action):

    def name(self) -> Text:
        return "action_tomorrow_weather"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

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

        dispatcher.utter_message(text=text)

        return []

class ActionTomorrowSunnyCloudy(Action):

    def name(self) -> Text:
        return "action_tomorrow_sunny_cloudy"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call_tomorrow)

        day_num = 1

        description = response.json()["daily"][day_num]["weather"][0]["description"]

        text = "Tomorrow's sky: " + description

        dispatcher.utter_message(text=text)

        return []

class ActionCurrentWind(Action):

    def name(self) -> Text:
        return "action_current_wind"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call)

        wind_speed = int(response.json()["wind"]["speed"])

        if wind_speed<=24:
            text_wind = "Today it is not very windy. "
        else:
            text_wind = "Today it is a windy day. "

        text = text_wind + "Current wind speed is " + str(wind_speed) + "km/h"

        dispatcher.utter_message(text=text)

        return []

class ActionSunnyCloudy(Action):

    def name(self) -> Text:
        return "action_sunny_cloudy"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(weather_api_call)

        description = response.json()["weather"][0]["description"]

        text = "Today's sky is: " + description

        dispatcher.utter_message(text=text)

        return []

class ActionGoodBye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        phrases = ["I hope I was helpful today, don't hesitate talking to me for more weather information!",
                    "Have a wonderful day! I will be here if you have more questions!",
                    "Talk to you later, bye!",
                    "Until next time!"]

        text = sample(phrases,1)[0]

        dispatcher.utter_message(text=text)

        return []
