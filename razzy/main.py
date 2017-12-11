from commands import *
import sys
import os
from senses import *

# Get senses locally
brain  = Brain()
ears   = Ears()
mouth  = Mouth()
lights = Lights()
wheels = Wheels()
chat   = Chat()

currentState = "listen";

# train chat
chat.init()

try:
  #message = "go explore"

  mouth.speak(["Hello, my name is Razzy"])
  while True:
    # Turn on light when listening
    lights.redLight(1);
    lights.blueLight(0);
    lights.greenLight(0);

    message = ears.listen()

    # if message was empty, see if current state has a continue
    if (message == "" and currentState !='listen'):
      currentState = brain.getCurrentState()
      commandClass = globals()[currentState]
      commandClass().doContinue(message)
      
    lights.redLight(0);
    lights.blueLight(1);

    print "You said '" + message + "'"
    command = brain.checkMessage(message);
    print command

    # if we have a command, run it
    if (command):
      # Turn off light when command is recieved
      lights.blueLight(0);
      lights.greenLight(1);

      # Look for class named "command" in the list of commands
      commandClass = globals()[command]
      response = commandClass().run(message)
      # code 200 is speak and continue
      if (response.code == CommandResponse.CODE_OK):
        mouth.speak(response.message)
      # code 0 is speak and exit
      elif (response.code == CommandResponse.CODE_EXIT):
        mouth.speak(response.message)
      print "done command"
    # otherwise default to chatting
    else:
      reply = chat.reply(message)
      mouth.speak([reply])
    print "keep looping"
    
    message = ''
finally:
  lights.cleanup()
  wheels.stop()