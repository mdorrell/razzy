import speech_recognition as sr
import pyaudio

class Ears():

  def listen(self):
    r = sr.Recognizer()
    message = ""
    
    #Microphone(device_index=i, sample_rate=48000)
    with sr.Microphone( sample_rate=48000) as source:
      r.pause_threshold       = 0.5     # seconds of non-speaking audio before a phrase is considered complete
      r.phrase_threshold      = 0.5     # minimum seconds of speaking audio before we consider the speaking audio a phrase 
      r.non_speaking_duration = 0.5     # seconds of non-speaking audio to keep on both sides of the recording
      r.energy_threshold      = 1000    # Higher number makes the mic less sensitive
      r.dynamic_energy_threshold = False
      
      #r.adjust_for_ambient_noise(source)
      try:
        audio = r.listen(source, timeout = 10)
        message = r.recognize_google(audio)    
      except sr.WaitTimeoutError as e:
        print "Listen timeout"   
        message = ""
      except sr.UnknownValueError:     
        message = ""
      except sr.RequestError as e:
        message = ""

    return message
  