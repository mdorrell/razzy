import sys
import os
from senses import *

class Razzy():
  
  # Get senses locally
  brain  = Brain()
  ears   = Ears()
  mouth  = Mouth()
  lights = Lights()
  wheels = Wheels()
  chat   = Chat()
  
  currentState = '';
  
  def getBrain(self):
    return self.brain
  
  def getEars(self):
    return self.ears
  
  def getMouth(self):
    return self.mouth
  
  def getLights(self):
    return self.lights
  
  def getWheels(self):
    return self.wheels
  
  def getChat(self):
    return self.chat
  
  """
  Initializes razzy
  """
  def init(self):
    # train chat
    #chat.init()
    
    self.currentState = "listen";
    self.getMouth().speak(["Hello, my name is Razzy"])

  """
  Main function while razzy is running
  """
  def run(self):
    # Get users command
    message = self.getMessage()

    # Check if we must run a continue command
    self.doContinue(message)

    # Check if we have a command for the message
    command = self.getCommand(message)

    # If we have a command, run it
    if (command):
      
      # run the command
      self.processCommand(command)

    # If we don't have a command do default action
    else:
      self.doDefaultAction(message)
    
    print "keep looping"
    
    message = ''
  
  """
  Get message from user
  :returns string message - What the user said
  """
  def getMessage(self):
        
    # Turn on red light when listening
    self.getLights().redLight(1);
    self.getLights().blueLight(0);
    self.getLights().greenLight(0);

    print "Listening"
    currentState = self.getBrain().getCurrentState()
    listenTime   = self.getEars().getPhraseTimeout(currentState)
    message      = self.getEars().listen(listenTime)

    print message
    
    return message
  
  """
  If message was empty
  and current state has a continue command process it
  :param string message - What the user said
  """
  def doContinue(self, message):
        
    # if message was empty, see if current state has a continue
    if (message == "" and self.currentState !='listen'):
      currentState = self.getBrain().getCurrentState()
      commandClass = globals()[currentState]
      commandClass().doContinue(message)
    
  """
  Get command from message if we have one
  :returns CommandBase command - Command class we will execute
  """
  def getCommand(self, message):
        
    # Blue light when processing command
    self.getLights().redLight(0);
    self.getLights().blueLight(1);

    print "You said '" + message + "'"
    command = self.getBrain().checkMessage(message);
    print command
    
  """
  Run the given command
  :param CommandBase command - Command we will run
  """
  def processCommand(self, command):
    # Green light when we run command
    self.getLights().blueLight(0);
    self.getLights().greenLight(1);

    # Look for class named "command" in the list of commands
    commandClass = globals()[command]
    response = commandClass().run(message)
    
    # code 200 is speak and continue
    if (response.code == CommandResponse.CODE_OK):
      self.getMouth().speak(response.message)
    # code 0 is speak and exit
    elif (response.code == CommandResponse.CODE_EXIT):
      self.getMouth().speak(response.message)
      
    print "done command"
    
  """
  Do what we do when we don't have a command for the message
  :param string message - What the user said
  """
  def doDefaultAction(self, message):
    #reply = chat.reply(message)
    #mouth.speak([reply])
    self.getMouth().speak([message])
      
  """
  Shutdown razzy properly
  """
  def shutdown(self):
    self.getLights().cleanup()
    self.getWheels().stop()