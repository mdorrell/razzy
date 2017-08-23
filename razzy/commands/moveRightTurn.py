import abc
import imp
import sys
import os

from commandBase import CommandBase
from commandResponse import CommandResponse

class MoveRightTurn(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    return ["turn", "right"]
    
  def run(self, message):
    print "Turn right"
    self.loadWheels()
    self.wheels.right(5)
    
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