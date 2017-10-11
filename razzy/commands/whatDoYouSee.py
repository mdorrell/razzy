import abc
import senses.eyes

from commandBase import CommandBase
from commandResponse import CommandResponse

class WhatDoYouSee(CommandBase):
  eyes = ''
  
  responses = [
    "I see {0}",
    "It looks like {0}",
    "It is {0}"
  ]
  
  @staticmethod
  def getKeywords(self):
    return ["what", "see"]
    
  def run(self, message):
    self.eyes = senses.Eyes()
    
    picPath = self.look()
    item    = self.identify(picPath)
    message = self.getResponse([item])

    response = CommandResponse(CommandResponse.CODE_OK, message);
    return response
  
  # Take a picture
  def look(self):
    picPath = self.eyes.look()
    self.identify(picPath)
    return picPath

  # say what you see 
  def identify(self, picPath):

    labels = self.eyes.identify(picPath)

    for label in labels:
        print label.description
        print label.score
        
    return labels[0].description