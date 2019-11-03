import os
import time

class Mouth():
    
  """
  Constructor
  """
  def __init__(self, logger):
    self.logger = logger
    
  def speak(self, lines):
    tts_engine = 'espeak -s150 --stdout '
    for line in lines:
      self.logger.info(line)
      os.system(tts_engine + ' "' + line + '" | aplay')
      time.sleep(.5)
    return