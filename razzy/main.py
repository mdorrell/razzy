from commands import *
import imp
import sys
import os

ROOT_FILEPATH = os.path.dirname(sys.modules['__main__'].__file__)
earsModule   = imp.load_source('senses', ROOT_FILEPATH + '/../senses/ears.py')
mouthModule  = imp.load_source('senses', ROOT_FILEPATH + '/../senses/mouth.py')
lightsModule = imp.load_source('senses', ROOT_FILEPATH + '/../senses/lights.py')

ears = earsModule.Ears()
mouth = mouthModule.Mouth()
lights = lightsModule.Lights()

mouth.speak(["Hello, my name is Razzy"])
while True:
  # Turn on light when listening
  lights.redLight(1);
  lights.redBlue(1);
  lights.redGreen(1);

  message = ears.listen()
  #message = "play nirvana"
  print "You said '" + message + "'"
  command = ears.checkMessage(message);
  print command
  if (command):
    # Turn off light when command is recieved
    lights.redLight(0);
    lights.redBlue(0);
    lights.redGreen(0);

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
