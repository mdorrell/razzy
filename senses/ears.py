import speech_recognition as sr
import pyaudio
import operator
from commands import COMMANDS

class Ears():

  def listen(self):
    r = sr.Recognizer()

    #Microphone(device_index=i, sample_rate=48000)
    with sr.Microphone( sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # This is to write to a file
    #with open("microphone-results.wav", "wb") as f:
    #    f.write(audio.get_wav_data())

    # recognize speech using Sphinx
    try:
        message = r.recognize_google(audio)
    except sr.UnknownValueError:
        message = "What did you say?"
    except sr.RequestError as e:
        message = "I don't feel very well, I need to lie down"

    return message
  
  def checkMessage(self, message):
    matches = {}
    message_words = message.split()
    for command in COMMANDS:
      if (set(set(COMMANDS[command])).issubset(message_words)):
        # make list of commands with count of words matched
        matches[command] = len(COMMANDS[command])

    # get command with highest number of words matched
    command = max(matches.iteritems(), key=operator.itemgetter(1))[0]

    return command