import abc
import sys
import os
import senses.wheels

from commandBase import CommandBase
from commandResponse import CommandResponse

class Stop(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["stop"])
    return keywords    
    
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self, message, razzy):
    return False
  
  def run(self, message, razzy):
    print "Stop"
    self.loadWheels(razzy.getLogger())
    self.wheels.stop()
    
    message = ''
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self, logger):
    self.wheels = senses.Wheels(logger)