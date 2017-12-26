import abc
import sys
import os
import senses.wheels

from commandBase import CommandBase
from commandResponse import CommandResponse

class MoveLeftTurn(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["turn", "left"])
    return keywords
    
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self, message):
    return False
  
  def run(self, message):
    print "Turn left"
    self.loadWheels()
    self.wheels.left()
    
    message = ''
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self):
    self.wheels = senses.Wheels()