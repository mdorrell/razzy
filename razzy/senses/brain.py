from commands import COMMANDS
import operator

class Brain():
  currentState = "listen"
  
  lastCommand = ""
  
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
    matches = {}
    message_words = message.split()
    for command in COMMANDS:
      for phrase in COMMANDS[command]:
        if (set(set(phrase)).issubset(message_words)):
          # make list of commands with count of words matched
          matches[command] = len(phrase)

    # get command with highest number of words matched
    if matches:   
      activeCommand = max(matches.iteritems(), key=operator.itemgetter(1))[0]

    # set last command
    self.lastCommand = activeCommand
    
    return activeCommand