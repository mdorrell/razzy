import abc
import senses.eyes

from commandBase import CommandBase
from commandResponse import CommandResponse

class WhatDoYouSee(CommandBase):
  
  @staticmethod
  def getKeywords(self):
    return ["what", "see"]
    
  def run(self, message):
    picPath = self.look()
    print picPath
    message   = ["I see you"]

    response = CommandResponse(CommandResponse.CODE_OK, message);
    return response
  
  # Get data from weather underground
  def look(self):
    eyes = senses.Eyes()
    picPath = eyes.look()
    return picPath

  