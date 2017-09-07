import abc
import re
import sys
import os
import senses.spotify

from commandBase import CommandBase
from commandResponse import CommandResponse

class PlayMusicSearch(CommandBase):
  spotify = ''
  
  responses = [
    "Playing {0}",
    "Next up is {0}",
  ]
  
  #---------------------
  # Keywords to initiate command
  #---------------------  
  @staticmethod
  def getKeywords(self):
    return ["play"]
  
  #---------------------
  # Run the command
  #---------------------    
  def run(self, message):
    keyword = self.parseMessage(message)
    self.loadSpotify();
    self.spotify.search(keyword)
    
    message = self.getResponse([keyword])
    response = CommandResponse(CommandResponse.CODE_OK, message)
    return response
     

  #---------------------
  # Get search keyword from the search string
  #---------------------
  def parseMessage(self, message):
    # Match anything between play and period, period is optional
    result = re.search('play ([^.]*).*', message)
    keyword = result.group(1)
    return keyword
  
  #-------------------------
  # load spotify
  #-------------------------
  def loadSpotify(self):
    self.spotify = senses.Spotify()