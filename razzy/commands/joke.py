import abc
import requests
import json

from commandBase import CommandBase
from commandResponse import CommandResponse

class Joke(CommandBase):
    
  @staticmethod
  def getKeywords(self):
    return ["tell", "joke"]
    
  def run(self, message):
    headers={'Accept': "application/json"}
    r = requests.get('https://icanhazdadjoke.com/', headers=headers)
    a = json.loads(r.text)
    print a
    message = [a['joke']]
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
