from __future__ import division
import time

class Wheels():
  # Default to no Pi
  hasPi = False
 
  # Configure min and max servo pulse lengths                                                                                            
  servo_min = 150  # Min pulse length out of 4096                                                                                        
  servo_max = 600  # Max pulse length out of 4096   

  # stores pwm reference
  pwm = '';
  
  #--------------------
  # Constructor
  #--------------------
  def __init__(self):

    # If we are using the Pi enable it
    self.hasPi = self.initPi()
  
  #---------------------------
  # Move forward
  #---------------------------
  def forward(self, time):
    self.moveWheels(self.servo_min, self.servo_max, time)

  #---------------------------
  # Move backwards
  #---------------------------
  def backwards(self, time):
    self.moveWheels(self.servo_max, self.servo_min, time)    

  #---------------------------
  # Turn right
  #---------------------------
  def right(self, time):
    self.moveWheels(self.servo_max, self.servo_max, time) 
  
  #---------------------------
  # Turn left
  #---------------------------
  def left(self, time):
    self.moveWheels(self.servo_min, self.servo_min, time) 
        
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
  
  #-------------------------------
  # Toggle light on or off
  #-------------------------------
  def moveWheels(self, left, right, time):   
    # if we have a Pi light it
    if (self.hasPi):  
      # Turn wheels on
      self.pwm.set_pwm(11, 0, left)
      self.pwm.set_pwm(4, 0, right)

      # Let them run
      time.sleep(time)
  
      # Stop the wheels
      pwm.set_pwm(11, 0, 0);
      pwm.set_pwm(4, 0, 0);

