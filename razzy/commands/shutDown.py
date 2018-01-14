import abc
from commandBase import CommandBase
from commandResponse import CommandResponse

class ShutDown(CommandBase):
  
  @staticmethod
  def getKeywords(self):
    keywords = []
    keywords.append(["sleep"])
    return keywords     
    
  #----------------------
  # doContinue
  #----------------------
  def doContinue(self, message, razzy):
    return False
  
  def run(self, message, razzy):
    message = ["Good night"]
    response = CommandResponse(CommandResponse.CODE_EXIT, message);
    return response
  
