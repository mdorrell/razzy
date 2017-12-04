import abc
import sys
import os
import senses.spotify

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
    keywords = []
    keywords.append(["stop", "playing"])
    return keywords     

  #----------------------
  # doContinue
  #----------------------
  def doContinue(self):
    return False

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
    self.spotify = senses.Spotify()