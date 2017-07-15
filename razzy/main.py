from senses import *
from commands import *
ears = Ears()
mouth = Mouth()
lights = Lights()

lights.redLight(1);
#mouth.speak(["Hello, my name is Razzy"])
while True:
  #message = ears.listen()
  message = "I want to watch Peppa Pig"
  print "You said '" + message + "'"
  command = ears.checkMessage(message);
  if (command):
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
    mouth.speak(message)

