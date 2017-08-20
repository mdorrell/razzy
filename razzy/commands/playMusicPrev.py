import abc
import imp
import sys
import os

from commandBase import CommandBase
from commandResponse import CommandResponse

class PlayMusicPrev(CommandBase):
  spotify = ''
  
  responses = [
    "Playing previous track",
    "Skipping back a song",
    "That was a good song"
  ]
  
  #---------------------
  # Keywords to initiate command
  #---------------------  
  @staticmethod
  def getKeywords(self):
    return ["go", "back"]
  
  #---------------------
  # Run the command
  #---------------------    
  def run(self, message):
    self.loadSpotify();
    self.spotify.back()
    
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
     