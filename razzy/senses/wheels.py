from __future__ import division
import time
import senses.radar as radar

class Wheels():
  # Default to no Pi
  hasPi = False
 
  # Configure min and max servo pulse lengths                                                                                            
  servo_min = 150  # Min pulse length out of 4096                                                                                        
  servo_max = 600  # Max pulse length out of 4096   

  # stores pwm reference
  pwm = '';
  
  """
  Constructor
  """
  def __init__(self, logger):
    self.logger = logger

    # If we are using the Pi enable it
    self.hasPi = self.initPi()
  
  #---------------------------
  # Move forward
  #---------------------------
  def forward(self):
    return self.moveWheels(self.servo_min, self.servo_max)

  #---------------------------
  # Move backwards
  #---------------------------
  def backwards(self):
    return self.moveWheels(self.servo_max, self.servo_min)    

  #---------------------------
  # Turn right
  #---------------------------
  def right(self):
    return self.moveWheels(self.servo_max, self.servo_max) 
  
  #---------------------------
  # Turn left
  #---------------------------
  def left(self):
    return self.moveWheels(self.servo_min, self.servo_min) 
  
  #---------------------------
  # Stop moving
  #---------------------------
  def stop(self):
    self.moveWheels(0, 0)
    
  #----------------------------------
  # stuff we need to do tp setup the pwm
  #----------------------------------
  def initPi(self):
    try:
      import Adafruit_PCA9685
      self.pwm = Adafruit_PCA9685.PCA9685()
     
      # Set frequency to 60hz, good for servos.                                                                                              
      self.pwm.set_pwm_freq(60)

      return True
    except ImportError:
      return False
    else:
      return False
  
  #--------------------------------
  # Check if there is room to move
  #--------------------------------
  def checkIsClear(self):
    isClear = True
    r = radar.Radar()
    distance = r.getDistance()
    
    if (distance < 30):
      #if we got 0 it might be an error try again
      if (distance == 0):
        distance = r.getDistance()

        # must have been right
        if (distance == 0):
          isClear = False
      else:
        isClear = False
      
    return isClear
    
  #-------------------------------
  # Toggle light on or off
  # @returns bool true if clear false if blocked
  #-------------------------------
  def moveWheels(self, left, right):   
    isClear = True
    
    # if we have a Pi light it
    if (self.hasPi):  
      # Turn wheels on
      self.pwm.set_pwm(11, 0, left)
      self.pwm.set_pwm(4, 0, right)

      # Let them run
      #for x in range(0, waitTime-1):
      # only check if moving forward
      if (left == self.servo_min and right == self.servo_max):
        isClear = self.checkIsClear()

        # if we don't have room, stop moving
        if not isClear:
          # Stop the wheels
          self.pwm.set_pwm(11, 0, 0);
          self.pwm.set_pwm(4, 0, 0);
        
      #time.sleep(1)
      
    return isClear

