import abc
import sys
import os
import senses.spotify

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
    self.spotify = senses.Spotify()
     