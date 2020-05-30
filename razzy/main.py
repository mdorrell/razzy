from commands import *
from razzy import Razzy

import sys
import os
import time
import speech_recognition as sr

# Load razzy 
razzy  = Razzy()

# def callback(recognizer, audio):                          # this is called from the background thread
#     try:
#         if (audio):
#           message = r.recognize_google(audio)
#         else:
#           message = ''
#
#         #message = recognizer.recognize(audio)
#         print("You said " + message)  # received audio data, now need to recognize it
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except LookupError:
#         print("Oops! Didn't catch that")
# r = sr.Recognizer()
# r.pause_threshold = 0.25  # seconds of non-speaking audio before a phrase is considered complete
# r.phrase_threshold = 0.5  # minimum seconds of speaking audio before we consider the speaking audio a phrase
# r.non_speaking_duration = 0.25  # seconds of non-speaking audio to keep on both sides of the recording
# r.energy_threshold = 1000  # Higher number makes the mic less sensitive
# r.dynamic_energy_threshold = False
# m = sr.Microphone()
# with m as source: r.adjust_for_ambient_noise(source)      # we only need to calibrate once, before we start listening
# stop_listening = r.listen_in_background(m, callback)


try:
  doShutdown = False;

  commands = globals()

  # Initialize razzy
  razzy.init(commands)
  while not doShutdown:
    
    # Each loop listens for a command and processes it
    doShutdown = razzy.run()

    # wait for next loop
    time.sleep(1)
    #stop_listening()                                          # call the stop function to stop the background thread


finally:
  # Shutdown properly
  razzy.shutdown()
