import abc
import requests
from commandBase import CommandBase
from commandResponse import CommandResponse
from datetime import datetime
import re

class Weather(CommandBase):
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["what", "weather"])
    return keywords     
    
  def run(self, message):
    data = self.getData()
    now       = self.filterMessage(data["forecast"]['txt_forecast']['forecastday'][0]['fcttext'])
    laterName = data["forecast"]['txt_forecast']['forecastday'][1]['title']
    later     = self.filterMessage(data["forecast"]['txt_forecast']['forecastday'][1]['fcttext'])
    lastName  = data["forecast"]['txt_forecast']['forecastday'][2]['title']
    last      = self.filterMessage(data["forecast"]['txt_forecast']['forecastday'][2]['fcttext'])

    messageNow   = "Right now it is " + now
    messageLater = laterName + " it will be " + later
    messageLast  = lastName + " it will be " + last
    message      = [messageNow, messageLater, messageLast]

    response = CommandResponse(CommandResponse.CODE_OK, message);
    return response
  
  # Get data from weather underground
  def getData(self):
    urlNow = "http://api.wunderground.com/api/1144d89f29eb17c0/forecast/q/CA/San_Diego.json"

    r = requests.get(urlNow)
    data = r.json()
    return data
  
  # Replace test in the messages we get back
  def filterMessage(self, message):
    # replace (digit)(space)(mph) with (digit)(space)(miles per hour)
    message = re.sub('(\d.\s)(mph)', '\g<1>miles per hour', message)
  
    # replace (digit)(F) with (digit)( degrees)
    message = re.sub('(\d)(F)', '\g<1> degrees', message)
  
    # replace Winds (direction letter) with direction name
    message = re.sub('(Winds)\s(N)(.*)\s', '\g<1> North \g<3>', message)
    message = re.sub('(Winds)\s(S)(.*)\s', '\g<1> South \g<3>', message)
    message = re.sub('(Winds)\s(E)(.*)\s', '\g<1> East \g<3>', message)
    message = re.sub('(Winds)\s(W)(.*)\s', '\g<1> West \g<3>', message)
    message = re.sub('(Winds)\s(.*)(NE)(.*)', '\g<1> \g<2> North East \g<4>', message)
    message = re.sub('(Winds)\s(.*)(SE)(.*)', '\g<1> \g<2> South East \g<4>', message)
    message = re.sub('(Winds)\s(.*)(SW)(.*)', '\g<1> \g<2> South West \g<4>', message)
    message = re.sub('(Winds)\s(.*)(NW)(.*)', '\g<1> \g<2> North West \g<4>', message)

    return message
  