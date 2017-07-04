import abc
import pywapi
from commandBase import CommandBase
from commandResponse import CommandResponse
from datetime import datetime

class Weather(CommandBase):
  
  @staticmethod
  def getKeywords(self):
    return ["what", "weather"]
    
  def run(self):
    #bostonweather = pywapi.get_weather_from_weather_com('UKXX1701', 'metric')
    #message = ("In Boston, Lincolnshire it is currently: " + str(bostonweather['current_conditions']['text']).lower() + " and " + str(bostonweather['current_conditions']['temperature']).lower());
    message = "The weather is nice"
    response = CommandResponse(CommandResponse.CODE_OK, message);
    return response
  
