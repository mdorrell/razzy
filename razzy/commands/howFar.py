import abc
import sys
import senses.radar

from commandBase import CommandBase
from commandResponse import CommandResponse

class HowFar(CommandBase):
  
  # reference to radar
  radar = ''

  responses = [
    "It is clear for {0} centimeters",
    "I can see for {0} centimeters",
    "{0} centimeters"
  ]
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["how", "far", "front"])
    keywords.append(["how", "far", "see"])
    return keywords
  
  def run(self, message):
    print "How far in front of me"
    self.loadRadar()
    distance = self.radar.getDistance()
    
    message = self.getResponse([distance])
    response = CommandResponse(CommandResponse.CODE_OK, message);  
    return response
  
  #-------------------------
  # load radar
  #-------------------------
  def loadRadar(self):
    self.radar = senses.Radar()