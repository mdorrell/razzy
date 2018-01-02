from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chat():
  #stores the chatterbot class
  chatterbot = ''
  
  """
  Constructor
  """
  def __init__(self, logger):
    self.logger = logger
    
  """
  Initialize chatbot
  """
  def init(self):
    self.chatterbot = ChatBot("Razzy")
    self.chatterbot.set_trainer(ChatterBotCorpusTrainer)

    self.chatterbot.train("chatterbot.corpus.english")
    
  def reply(self, message):
    # Get a response to the input text 'How are you?'
    response = self.chatterbot.get_response(message)

    print(response)
    return str(response)
    