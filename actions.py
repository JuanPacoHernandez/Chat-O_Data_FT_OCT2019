from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		api_key='Your API key here"
		loc=tracker.get_slot('location')
		api_address='http://api.apixu.com/v1/current.json?key={}&q={}'.format(api_key,loc)  
		current=requests.get(api_address).json()		
		country=current['location']['country']
		city=current['location']['name']
		condition=current['current']['condition']['text']
		temperature_c=current['current']['temp_c']
		humidity=current['current']['humidity']

		response="""En este momento hay {} en {}. La temperatura es {} °C y la humedad relativa es {}%""".format(condition, city,temperature_c,humidity)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

