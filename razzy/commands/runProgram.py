import abc
import sys
import os
import senses.wheels
import time

from commandBase import CommandBase
from commandResponse import CommandResponse

class RunProgram(CommandBase):
  
  # reference to wheels
  wheels = ''
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["run", "program"])
    keywords.append(["execute", "program"])
    keywords.append(["start", "program"])
    return keywords
  
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self, message, razzy):
    return False
  
  def run(self, message, razzy):
    print("Running Run Program")
    self.loadWheels(razzy.getLogger())
    
    razzy.getMouth().speak(["Running program 1"])

    program = self.loadProgram();
    
    self.processProgram(program)
    
    #self.wheels.backwards()
    
    message = ''
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  """
  Load the program from disk
  """
  def loadProgram(self):
    scriptDir = os.path.dirname(__file__) #<-- absolute dir the script is in
    programPath = "../programs/program1.txt"
    fullPath = os.path.join(scriptDir, programPath)
    print(fullPath)
    
    with open(fullPath) as f:
      program = f.readlines()
      
    return program

  """
  Process the program
  :param List program - all the commands in the program
  """
  def processProgram(self, program):
    for line in program:
      command = line.split()
      
      direction = command[0]
      duration  = command[1]
      
      print("running command {} {}".format(direction, duration))
      
      # Move in the right direction
      if (direction == 'F'):
        self.wheels.forward()
      elif (direction == 'R'):
        self.wheels.right()
      elif (direction == 'L'):
        self.wheels.left()
      elif (direction == 'B'):
        self.wheels.backwards()
      
      # wait for time of duration
      time.sleep(float(duration))
      
      #stop the wheels
      self.wheels.stop()
      
      
  #-------------------------
  # load wheels
  #-------------------------
  def loadWheels(self, logger):
    self.wheels = senses.Wheels(logger)