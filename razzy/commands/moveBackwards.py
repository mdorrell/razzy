import abc
import imp
import sys
import os

from commandBase import CommandBase
from commandResponse import CommandResponse

class MoveBackwards(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    return ["move", "backwards"]
    
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
    root = os.path.dirname(sys.modules['__main__'].__file__)
    path = root + '/../senses/wheels.py'
    
    senses = imp.load_source('senses', path)
    self.wheels = senses.Wheels()