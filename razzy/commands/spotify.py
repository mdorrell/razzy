import abc
from commandBase import CommandBase
from commandResponse import CommandResponse

class Spotify(CommandBase):
  
  @staticmethod
  def getKeywords(self):
    return ["play"]
    
  def run(self):
    message = ["I will play"]
    response = message;
    return response
  