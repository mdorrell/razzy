
class Lights():
  # Default to no Pi
  hasPi = False

  # pin number of green led 
  greenLed = 6
  blueLed  = 24
  redLed   = 12

  # stores gpio reference
  gpio = '';
  
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
  # toggle green light status
  #---------------------------
  def greenLight(self, isOn):
    self.toggleLight("Green", self.greenLed, isOn)

  #---------------------------
  # toggle red light status
  #---------------------------
  def blueLight(self, isOn):
    self.toggleLight("Blue", self.blueLed, isOn)

  #---------------------------
  # Cleanup 
  #---------------------------     
  def cleanup(self):
    if self.hasPi:
      self.gpio.cleanup()

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
      GPIO.setup(self.blueLed, GPIO.OUT)
      self.gpio = GPIO
      
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
      self.gpio.output(light, isOn)

  
  def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True