import speech_recognition as sr
import pyaudio
import senses.brain as brain

class Ears():
  brain  = brain.Brain()

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
        
        # This is to write to a file
        #with open("microphone-results.wav", "wb") as f:
        #    f.write(audio.get_wav_data())
        phraseTimeout = self.getPhraseTimeout()
        
        audio = r.listen(source, timeout = 10, phrase_time_limit=phraseTimeout)
        message = r.recognize_google(audio)    
      except sr.WaitTimeoutError as e:
        print "Listen timeout"   
        message = ""
      except sr.UnknownValueError:     
        message = ""
      except sr.RequestError as e:
        message = ""

    return message
  
  #-------------------------------------
  # Get how long we listen for
  #-------------------------------------
  def getPhraseTimeout(self):
    # get the current state
    currentState = self.brain.getCurrentState()

    # List of states where wheels are moving
    movementStates = [
      'MoveRightTurn',
      'MoveLeftTurn',
      'MoveBackwards',
      'MoveForward'
    ]
    
    # Movement states are loud, so wait less time
    if currentState in movementStates:
      phraseTimeout = 2
    else:
      phraseTimeout = 10
      
    return phraseTimeout
  