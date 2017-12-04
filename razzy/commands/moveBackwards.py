import abc
import sys
import os
import senses.wheels

from commandBase import CommandBase
from commandResponse import CommandResponse

class MoveBackwards(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["move", "backwards"])
    keywords.append(["go", "backwards"])
    return keywords
  
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self):
    return False
  
  def run(self, message):
    print "Move backwards"
    self.loadWheels()
    self.wheels.backwards(5)
    
    message = ''
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self):
    self.wheels = senses.Wheels()