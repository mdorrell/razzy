import abc
import imp

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
    senses = imp.load_source('senses', '/home/mdorrell/sites/razzy/senses/spotify.py')
    self.spotify = senses.Spotify()
    self.spotify.back()
    
    message = self.getResponse([])
    response = CommandResponse(CommandResponse.CODE_OK, message)
    return response
     