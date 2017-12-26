import abc
import sys
import os
import senses.wheels

from commandBase import CommandBase
from commandResponse import CommandResponse

class MoveRightTurn(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["turn", "right"])
    return keywords    
    
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self, message):
    return False
  
  def run(self, message):
    print "Turn right"
    self.loadWheels()
    self.wheels.right()
    
    message = ''
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self):
    self.wheels = senses.Wheels()