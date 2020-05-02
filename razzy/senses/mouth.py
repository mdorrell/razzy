import os
import time

class Mouth():
    
  """
  Constructor
  """
  def __init__(self, logger, ears):
    self.logger = logger
    self.ears   = ears
    
  def speak(self, lines):

    if (lines[0]):
      self.ears.stopListening()

      tts_engine = 'espeak -s150 --stdout '
      for line in lines:
        self.logger.info(line)
        os.system(tts_engine + ' "' + line + '" | aplay')
        time.sleep(.5)

      self.ears.listenInBackground()

    return