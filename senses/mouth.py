import os
import time

class Mouth():
    
  def speak(self, lines):
    tts_engine = 'espeak'
    for line in lines:
      print line
      os.system(tts_engine + ' "' + line + '"')
      time.sleep(.5)
    return