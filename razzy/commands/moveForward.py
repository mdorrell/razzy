import abc
import sys
import os
import senses.wheels

from commandBase import CommandBase
from commandResponse import CommandResponse

class MoveForward(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["move", "forward"])
    keywords.append(["go", "forward"])
    return keywords
    
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self):
    return False
  
  def run(self, message):
    print "Move forward"
    self.loadWheels()
    self.wheels.forward(5)
    
    message = ''
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self):
    self.wheels = senses.Wheels()