from commands import *
from razzy import Razzy

import sys
import os
import time
import speech_recognition as sr

# Load razzy 
razzy  = Razzy()

def callback(recognizer, audio):                          # this is called from the background thread
    try:
        if (audio):
          print("yes")
        else:
          print("no")
            
        message = r.recognize_google(audio)
        #message = recognizer.recognize(audio)
        print("You said " + message)  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! Didn't catch that")
r = sr.Recognizer()
m = sr.Microphone()
with m as source: r.adjust_for_ambient_noise(source)      # we only need to calibrate once, before we start listening
stop_listening = r.listen_in_background(m, callback)


try:
  doContinue = True;

  commands = globals()

  # Initialize razzy
  razzy.init(commands)
  while doContinue:
    
    # Each loop listens for a command and processes it
    #doContinue = razzy.run()

    print("looping")

    # wait for next loop
    time.sleep(1)
    #stop_listening()                                          # call the stop function to stop the background thread


finally:
  # Shutdown properly
  razzy.shutdown()
