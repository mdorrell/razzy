import speech_recognition as sr
import pyaudio
import time

class Ears():

  stop_listening = '';

  mic = ''

  """
  Constructor
  """
  def __init__(self, logger, brain):
    self.logger = logger
    self.brain = brain

    # Setup recognizer
    self.recognizer = sr.Recognizer()
    self.recognizer.pause_threshold          = 0.25  # seconds of non-speaking audio before a phrase is considered complete
    self.recognizer.phrase_threshold         = 0.5  # minimum seconds of speaking audio before we consider the speaking audio a phrase
    self.recognizer.non_speaking_duration    = 0.25  # seconds of non-speaking audio to keep on both sides of the recording
    self.recognizer.energy_threshold         = 1000  # Higher number makes the mic less sensitive
    self.recognizer.dynamic_energy_threshold = False

    # setup microphone
    self.mic = sr.Microphone()
    with self.mic as source:
        self.recognizer.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

  """
  " stopListening
  """
  def stopListening(self):

    if (self.stop_listening):
        self.stop_listening()

  """
  " listenInBackground
  """
  def listenInBackground(self):
    self.stop_listening = self.recognizer.listen_in_background(self.mic, self.listenInBackgroundCallback)

  """
  " listenInBackgroundCallback
  """
  def listenInBackgroundCallback(self, recognizer, audio):                          # this is called from the background thread
    try:
        if (audio):
          message = self.recognizer.recognize_google(audio)
        else:
          message = ''

        if (message):
            self.brain.setMemory('ears', message)

        print("I heard " + message)  # received audio data, now need to recognize it
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except LookupError:
        print("Oops! Didn't catch that")

  """
  " hearLastCommand
  """
  def hearLastCommand(self):
    command = self.brain.getMemory('ears')
    self.brain.setMemory('ears', '')
    return command