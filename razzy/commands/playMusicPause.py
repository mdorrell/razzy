import abc
import imp

from commandBase import CommandBase
from commandResponse import CommandResponse

class PlayMusicPause(CommandBase):
  spotify = ''
  
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
    senses = imp.load_source('senses', '/home/mdorrell/sites/razzy/senses/spotify.py')
    self.spotify = senses.Spotify()
    self.spotify.pause()
    
    message = self.getResponse([])
    response = CommandResponse(CommandResponse.CODE_OK, message)
    return response
     