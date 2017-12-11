import abc
import sys
import os
import random
import senses.wheels

from commandBase import CommandBase
from commandResponse import CommandResponse

class Explore(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["go", "explore"])
    keywords.append(["explore", "house"])
    return keywords
    
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self, message):
    print "continueing"
    
    self.run('')
    return True
    
  def run(self, message):
    print "Explore"
    self.loadWheels()
    isClear = True
    
    print "Move forward"
    isClear = self.wheels.forward(5)      

    if not isClear:
      print "not clear"
      isClear = self.doTurn()
        
    message = ''
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self):
    self.wheels = senses.Wheels()
    
  #-------------------------
  # doTurn
  # @returns boolean isClear true if front is clear false if it is blocked
  #-------------------------
  def doTurn(self):
    direction = random.randint(0,1)
    
    # turn left
    if (direction == 0):
      isClear = self.wheels.left(3)
    else:
      isClear = self.wheels.right(3)

    return isClear