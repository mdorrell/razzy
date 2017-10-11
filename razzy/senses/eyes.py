import sys
import io
import os
import pygame
from pygame.locals import *
import pygame.camera

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

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
    lookPath = self.picPath + 'look.png'
    self.cam.start()
    image = self.cam.get_image()
    pygame.image.save(image, lookPath)
    self.cam.stop()
    return lookPath

  #---------------------------------------
  # use google vision to see what you see
  #---------------------------------------
  def identify(self, picPath):

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(picPath, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels
