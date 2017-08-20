import abc
import imp
import sys
import os

from commandBase import CommandBase
from commandResponse import CommandResponse

class PlayMusicPause(CommandBase):
  
  responses = [
    "Stopping song",
    "Pausing song"
  ]
  
  #---------------------
  # Keywords to initiate command
  #---------------------  
  @staticmethod
  def getKeywords(self):
    return ["stop", "playing"]
  
  #---------------------
  # Run the command
  #---------------------    
  def run(self, message):
    self.loadSpotify();
    self.spotify.pause()
    
    message = self.getResponse([])
    response = CommandResponse(CommandResponse.CODE_OK, message)
    return response
     
  #-------------------------
  # load spotify
  #-------------------------
  def loadSpotify(self):
    root = os.path.dirname(sys.modules['__main__'].__file__)
    spotifyPath = root + '/../senses/spotify.py'
    
    senses = imp.load_source('senses', spotifyPath)
    self.spotify = senses.Spotify()