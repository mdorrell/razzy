import abc
from commandBase import CommandBase
from commandResponse import CommandResponse
from datetime import datetime

class Clock(CommandBase):
  
  responses = [
    "The time is now {0}",
    "It is {0}",
    "Right now it's {0}",
    "{0}"
  ]
  
  @staticmethod
  def getKeywords(self):
    return ["what", "time"]
    
  def run(self, message):
    time = datetime.strftime(datetime.now(), '%H:%M:%S')
    #message = ["The time is now " + time]
    message = self.getResponse([time])
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response