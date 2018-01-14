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
  def doContinue(self, message, razzy):
    return False
  
  def run(self, message, razzy):
    print "Move forward"
    self.loadWheels(razzy.getLogger())
    self.wheels.forward()
    
    message = ''
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self, logger):
    self.wheels = senses.Wheels(logger)