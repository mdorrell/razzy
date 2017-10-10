import sys
import os
import pygame
from pygame.locals import *
import pygame.camera

class Eyes():

  # path to sp
  root    = os.path.dirname(sys.modules['__main__'].__file__) 
  picPath = root + '/../pics/'
  cam     = ''
  
  #--------------------
  # Constructor
  #--------------------
  def __init__(self):
    pygame.init()
    pygame.camera.init()
    self.cam = pygame.camera.Camera("/dev/video0",(352,288))
  
  #----------------------------------
  # Take a picture save it on disk
  #----------------------------------
  def look(self):
    lookPath = self.picPath + 'look.bmp'
    self.cam.start()
    image = self.cam.get_image()
    pygame.image.save(image, lookPath)
    self.cam.stop()
    return lookPath
