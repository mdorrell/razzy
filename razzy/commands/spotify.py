import abc
import re
import subprocess
import time

from commandBase import CommandBase
from commandResponse import CommandResponse

class Spotify(CommandBase):
  # path to sp
  spPath = '/home/mdorrell/sites/razzy/bin/sp'
  
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
    self.openSpotify()
    self.search(keyword)
    
    message = ["I will play " + keyword]
    response = CommandResponse(CommandResponse.CODE_OK, message)
    return response
  
  #---------------------
  # Open spotify if it isn't already
  #---------------------
  def openSpotify(self):
    try:
      isOpen = subprocess.check_output(self.spPath + " version", shell=True)
    except:
      subprocess.call("spotify &", shell=True)
     
  #---------------------
  # Search for music
  #---------------------
  def search(self, keyword):
    print "DO SEARCH"
    searchCommand = self.spPath + ' search "' + keyword + '"'
    subprocess.call(searchCommand, shell=True)

  #---------------------
  # Get search keyword from the search string
  #---------------------
  def parseMessage(self, message):
    # Match anything between play and period, period is optional
    result = re.search('play ([^.]*).*', message)
    keyword = result.group(1)
    return keyword