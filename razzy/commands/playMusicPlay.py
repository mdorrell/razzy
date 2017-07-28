import abc
import imp

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
    senses = imp.load_source('senses', '/home/mdorrell/sites/razzy/senses/spotify.py')
    self.spotify = senses.Spotify()
    self.spotify.play()
    
    message = self.getResponse([])
    response = CommandResponse(CommandResponse.CODE_OK, message)
    return response
     