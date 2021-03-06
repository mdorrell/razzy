import subprocess
import sys
import os

class Spotify():
  # path to sp
  root = os.path.dirname(sys.modules['__main__'].__file__) 
  spPath = root + '/../bin/sp'
  
  """
  Constructor
  """
  def __init__(self, logger):
    self.logger = logger
    
    # Make sure spotify is open
    self.openSpotify()
  
  #---------------------
  # Open spotify if it isn't already
  #---------------------
  def openSpotify(self):
    try:
      isOpen = subprocess.check_output(self.spPath + " version", shell=True)
    except:
      subprocess.call("spotify &", shell=True)
      
  #---------------------
  # Search for music
  #---------------------
  def search(self, keyword):
    command = self.spPath + ' search "' + keyword + '"'
    subprocess.call(command, shell=True)

  def skip(self):
    command = self.spPath + ' next'
    subprocess.call(command, shell=True)
    
  def back(self):
    command = self.spPath + ' prev'
    subprocess.call(command, shell=True)
    
  def pause(self):
    command = self.spPath + ' pause'
    subprocess.call(command, shell=True)
        
  def play(self):
    command = self.spPath + ' play'
    subprocess.call(command, shell=True)

