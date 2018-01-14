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
    keywords = []
    keywords.append(["what", "see"])
    return keywords      
    
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self, message, razzy):
    return False
  
  def run(self, message, razzy):
    self.eyes = senses.Eyes(razzy.getLogger())
    
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

    ignore = [
      'red',
      'green',
      'blue',
      'black',
      'product',
    ]
    
    description = ''
    for label in labels:
        
        print label.description
        print label.score
        if label.description not in ignore:
          if label.score > .5:
            description = description + ', ' + label.description
          
    return description