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
    print("do continue")

    # Check if its clear, and if not we must stop
    self.loadWheels(razzy.getLogger())
    isClear = self.wheels.checkIsClear()

    if not isClear:
      self.wheels.stop()

    return False


  #----------------------
  # run
  #----------------------
  def run(self, message, razzy):
    print("Move forward")
    self.loadWheels(razzy.getLogger())
    isClear = self.wheels.forward()

    if (isClear):
      message = ''
    else:
      message = ['Something is in my way']

    response = CommandResponse(CommandResponse.CODE_OK, message);

    return response
  
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self, logger):
    self.wheels = senses.Wheels(logger)
