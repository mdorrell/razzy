import sys
import os
import traceback
import logging
from senses import *
from commands import CommandResponse

class Razzy():

  logger = ""
  commands = ""

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

  def getLogger(self):
    return self.logger

  """
  Constructor
  """
  def __init__(self):
    self.initLogger()

    # Get senses locally
    self.brain  = Brain(self.logger)
    self.ears   = Ears(self.logger, self.brain)
    self.mouth  = Mouth(self.logger, self.ears)
    self.lights = Lights(self.logger)
    self.wheels = Wheels(self.logger)
    #self.chat   = Chat(self.logger)
    self.chat   = ChatEcho(self.logger)

  """
  Initializes razzy
  """
  def init(self, commands):
    # train chat
    self.chat.init()

    self.commands = commands

    self.getMouth().speak(["Hello, my name is Razzy"])

  """
  Initialize Logger
  """
  def initLogger(self):
    self.logger = logging.getLogger(__name__)
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    out_hdlr.setLevel(logging.INFO)
    self.logger.addHandler(out_hdlr)
    self.logger.setLevel(logging.INFO)

  """
  Main function while razzy is running
  """
  def run(self):
    # Get users command
    #message = self.getMessage()
    message = self.ears.hearLastCommand()
    doShutdown = False;

    # check if we will repeat the same command
    if self.doContinue(message):
      command = self.getBrain().getCurrentState()
    else:
      # Check if we have a command for the message
      command = self.getCommand(message)

    # If we have a command, run it
    if (command):

      try:
        # run the command
        self.processCommand(command, message)
      except Exception:
        print("EXCEPTION: ")
        traceback.print_exc()
        self.getMouth().speak(["I'm afraid I can't do that"])

    # If we don't have a command do default action
    else:
      self.doDefaultAction(message)

    message = ''
    return doShutdown

  """
  Get message from user
  :returns string message - What the user said
  """
  def getMessage(self):

    # Turn on red light when listening
    self.getLights().redLight(1);
    self.getLights().blueLight(0);
    self.getLights().greenLight(0);

    currentState = self.getBrain().getCurrentState()
    listenTime   = self.getEars().getPhraseTimeout(currentState)
    message      = self.getEars().listen(listenTime)

    print(message)

    return message

  """
  If message was empty
  and current state has a continue command process it
  :param string message - What the user said
  """
  def doContinue(self, message):
    currentState = self.getBrain().getCurrentState()

    # if message was empty, see if current state has a continue
    if currentState != 'listen':
      commandClass = self.commands[currentState]
      return commandClass().doContinue(message, self)

  """
  Get command from message if we have one
  :returns CommandBase command - Command class we will execute
  """
  def getCommand(self, message):

    # Blue light when processing command
    self.getLights().redLight(0)
    self.getLights().blueLight(1)

    print("Parsing message '{}'".format(message))
    command = self.getBrain().checkMessage(message)

    if (command):
      print("Command is {}".format(command))
    else:
      print("Command not recognized")

    return command

  """
  Run the given command
  :param CommandBase command - Command we will run
  """
  def processCommand(self, command, message):
    # Green light when we run command
    self.getLights().blueLight(0)
    self.getLights().greenLight(1)

    # Look for class named "command" in the list of commands
    commandClass = self.commands[command]
    response = commandClass().run(message, self)

    # code 200 is speak and continue
    if (response.code == CommandResponse.CODE_OK):
      self.getMouth().speak(response.message)
    # code 0 is speak and exit
    elif (response.code == CommandResponse.CODE_EXIT):
      self.getMouth().speak(response.message)
      self.shutdown()
      exit()

  """
  Do what we do when we don't have a command for the message
  :param string message - What the user said
  """
  def doDefaultAction(self, message):
    message = self.chat.reply(message)
    self.getMouth().speak([message])

  """
  Shutdown razzy properly
  """
  def shutdown(self):
    self.getLights().cleanup()
    self.getWheels().stop()