import time

class Radar():
  # Default to no Pi
  hasPi = False
  
  # set the GPIO pin numbers
  trig = 21
  echo = 16
  
  # stores gpio reference
  gpio = ''
    
  #--------------------
  # Constructor
  #--------------------
  def __init__(self):

    # If we are using the Pi enable it
    self.hasPi = self.initPi()
    
  #----------------------------------
  # stuff we need to do to use GPIO
  #----------------------------------
  def initPi(self):
    try:
      import RPi.GPIO as GPIO
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.trig,GPIO.OUT)
      GPIO.setup(self.echo,GPIO.IN)
      self.gpio = GPIO
      
      return True
    except ImportError:
      return False
    else:
      return False  
    
  #---------------------------
  # Cleanup 
  #---------------------------     
  def cleanup(self):
    if self.hasPi:
      self.gpio.cleanup()
  
  def settleSensor(self):
    self.gpio.output(self.trig, False)
    time.sleep(0.5)

    self.gpio.output(self.trig, True)
    time.sleep(0.00001)
    self.gpio.output(self.trig, False)
    
  def getPulseStart(self):
    while self.gpio.input(self.echo)==0:
      pulseStart = time.time()
  
    return pulseStart
  
  def getPulseEnd(self):
    while self.gpio.input(self.echo)==1:
      pluseEnd = time.time()
      
    return pulseEnd

  # calculate the distance
  def calculateDistance(self, pulseStart, pulseEnd):
    pulseDuration = pulseEnd - pulseStart
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    
    return distance
  
  def getDistance(self):
  
    if (self.hasPi): 
      print "Distance Measurement In Progress"
    
      self.settleSensor()
      pulseStart = self.getStartTime()
      pulseEnd   = self.getPulseEnd();
      distance   = self.calculateDistance(pulseStart, pulseEnd)  
          
    else:
      print "Pi not found"
      distance = 0
      
    print "Distance:",distance,"cm"
    return distance
    