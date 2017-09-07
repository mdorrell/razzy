from commands import *
import sys
import os
from senses import *

ears = Ears()
mouth = Mouth()
lights = Lights()
wheels = Wheels()

try:
  mouth.speak(["Hello, my name is Razzy"])
  while True:
    # Turn on light when listening
    lights.redLight(1);
    lights.blueLight(0);
    lights.greenLight(0);

    #message = ears.listen()

    lights.redLight(0);
    lights.blueLight(1);

    message = "play nirvana"
    print "You said '" + message + "'"
    command = ears.checkMessage(message);
    print command
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
    else:
      mouth.speak([message])
    print "keep looping"
    exit()
finally:
  lights.cleanup()
  wheels.stop()