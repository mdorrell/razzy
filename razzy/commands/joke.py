import abc
import requests
import json
import unicodedata

from commandBase import CommandBase
from commandResponse import CommandResponse

class Joke(CommandBase):
    
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["tell", "joke"])
    return keywords
  
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self, message, razzy):
    return False
  
  def run(self, message, razzy):
    headers={'Accept': "application/json"}
    r = requests.get('https://icanhazdadjoke.com/', headers=headers)
    a = json.loads(r.text)

    # Assume the value object has proper __unicode__() method
    joke = a['joke']
    joke = unicodedata.normalize('NFKD', joke).encode('ascii', 'ignore')
    joke = joke.decode("utf-8")

    message = [joke]
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
