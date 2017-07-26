from senses import *
from commands import *
ears = Ears()
mouth = Mouth()
lights = Lights()

#mouth.speak(["Hello, my name is Razzy"])
while True:
  # Turn on light when listening
  lights.redLight(1);

  #message = ears.listen()
  message = "play Nirvana"
  print "You said '" + message + "'"
  command = ears.checkMessage(message);
  if (command):
    # Turn off light when command is recieved
    lights.redLight(0);
    # Look for class named "command" in the list of commands
    commandClass = globals()[command]
    response = commandClass().run()
    # code 200 is speak and continue
    if (response.code == CommandResponse.CODE_OK):
      mouth.speak(response.message)
      break
    # code 0 is speak and exit
    elif (response.code == CommandResponse.CODE_EXIT):
      mouth.speak(response.message)
      break
  else:
    mouth.speak([message])
  exit()
