import os

class Mouth():
    
  def speak(self, message):
    tts_engine = 'espeak'
    return os.system(tts_engine + ' "' + message + '"')
