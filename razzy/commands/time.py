import abc
from commandBase import CommandBase
from commandResponse import CommandResponse
from datetime import datetime

class Time(CommandBase):
  
  @staticmethod
  def getKeywords(self):
    return ["what", "time"]
    
  def run(self):
    time = datetime.strftime(datetime.now(), '%H:%M:%S')
    message = ["The time is now " + time]
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response