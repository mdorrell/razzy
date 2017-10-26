import abc
import requests
import json

from commandBase import CommandBase
from commandResponse import CommandResponse

class Joke(CommandBase):
    
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["tell", "joke"])
    return keywords
  
    
  def run(self, message):
    headers={'Accept': "application/json"}
    r = requests.get('https://icanhazdadjoke.com/', headers=headers)
    a = json.loads(r.text)

    # Assume the value object has proper __unicode__() method
    joke = unicode(a['joke'])

    print joke
    
    message = [joke]
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
