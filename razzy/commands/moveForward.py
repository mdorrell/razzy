import abc
import imp
import sys
import os

from commandBase import CommandBase
from commandResponse import CommandResponse

class MoveForward(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    return ["move", "forward"]
    
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
    root = os.path.dirname(sys.modules['__main__'].__file__)
    path = root + '/../senses/wheels.py'
    
    senses = imp.load_source('senses', path)
    self.wheels = senses.Wheels()