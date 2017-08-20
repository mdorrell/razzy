import abc
import imp
import sys
import os

from commandBase import CommandBase
from commandResponse import CommandResponse

class PlayMusicNext(CommandBase):
 
  spotify = ''
 
  responses = [
    "Playing next track",
    "Skipping to next song",
    "I didn't like this song either"
  ]
  
  #---------------------
  # Keywords to initiate command
  #---------------------  
  @staticmethod
  def getKeywords(self):
    return ["play", "next"]
  
  #---------------------
  # Run the command
  #---------------------    
  def run(self, message):
    self.loadSpotify();
    self.spotify.skip()

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
     