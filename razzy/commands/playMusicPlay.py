import abc
import imp
import sys
import os

from commandBase import CommandBase
from commandResponse import CommandResponse

class PlayMusicPlay(CommandBase):
  spotify = ''
  
  responses = [
    "Lets get back to the music",
    ""
  ]
  
  #---------------------
  # Keywords to initiate command
  #---------------------  
  @staticmethod
  def getKeywords(self):
    return ["start", "music"]
  
  #---------------------
  # Run the command
  #---------------------    
  def run(self, message):
    self.loadSpotify();
    self.spotify.play()
    
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