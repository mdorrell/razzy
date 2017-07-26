import abc
import os
from commandBase import CommandBase
from commandResponse import CommandResponse

class Spotify(CommandBase):
  
  @staticmethod
  def getKeywords(self):
    return ["play"]
    
  def run(self):
    self.search()
    message = ["I will play"]
    response = CommandResponse(CommandResponse.CODE_OK, message)
    return response
  
  def openSpotify(self):
    os.system("spotify")
  
  def search(self):
    os.system('/home/mdorrell/sites/razzy/bin/sp search "Nirvana"')