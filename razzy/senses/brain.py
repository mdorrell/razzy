from commands import COMMANDS
import operator

class Brain():
  currentState = "listen"
  
  lastCommand = ""

  memory = {}

  """
  Constructor
  """
  def __init__(self, logger):
    self.logger = logger
    
  def setCurrentState(self, state):
    self.currentState = state

  def getCurrentState(self):
    return self.currentState    
    
  def getLastCommand(self):
    return self.lastCommand
  
  #--------------------------------
  # See which command was requested
  # @return string activeCommand
  #---------------------------------
  def checkMessage(self, message):
    activeCommand = False;
    
    print("Current state {}".format(self.getCurrentState()))
    
    matches = {}
    message_words = message.split()
    
    for command in COMMANDS:
      for phrase in COMMANDS[command]:
        if (set(set(phrase)).issubset(message_words)):
          # make list of commands with count of words matched
          matches[command] = len(phrase)

    # get command with highest number of words matched
    if matches:   
      activeCommand = max(matches.items(), key=operator.itemgetter(1))[0]

    # set last command
    if activeCommand:
      self.lastCommand = activeCommand

      # set current state 
      self.setCurrentState(activeCommand)
    
    return activeCommand

  #--------------------------------
  # Save something to memory for later
  # @param string key
  # @param mixed value
  #--------------------------------
  def setMemory(self, key, value):
    self.memory[key] = value

  # --------------------------------
  # Return something save in memory
  # @param string key
  # @param mixed value
  # --------------------------------
  def getMemory(self, key):
    if key in self.memory.keys():
      value = self.memory[key]
    else:
      value = ''
    return value