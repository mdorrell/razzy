
class Lights():
  # Default to no Pi
  hasPi = False

  # pin number of green led 
  greenLed = 18
  redLed   = 23
  
  #--------------------
  # Constructor
  #--------------------
  def __init__(self):

    # If we are using the Pi enable it
    self.hasPi = self.initPi()
  
  #---------------------------
  # toggle red light status
  #---------------------------
  def redLight(self, isOn):
    self.toggleLight("Red", self.redLed, isOn)
  
  #---------------------------
  # toggle red light status
  #---------------------------
  def greenLight(self, isOn):
    self.toggleLight("Green", self.greenLed, isOn)
    
  #----------------------------------
  # stuff we need to do to use GPIO
  #----------------------------------
  def initPi(self):
    try:
      import RPi.GPIO as GPIO
      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.greenLed, GPIO.OUT)
      GPIO.setup(self.redLed, GPIO.OUT)
      return True
    except ImportError:
      return False
    else:
      return False
  
  #-------------------------------
  # Toggle light on or off
  #-------------------------------
  def toggleLight(self, name, light, isOn):
    # print status
    if (isOn):
      print name + " light is On"
    else:
      print name + " light is Off"
    
    # if we have a Pi light it
    if (self.hasPi):  
      GPIO.output(light, isOn)

  
  def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True