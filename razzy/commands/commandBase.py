import abc
from random import randint

class CommandBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def run(self, message):
        """Retrieve data from the input source and return an object."""
        return
    
    @abc.abstractmethod
    def getKeywords(self):
        """Return array of array of keywords."""
        return
    
    #--------------------------------------------------------
    #-- Used to get random responses
    #-- Define an array named "responses" in your subclass
    #-- Put in tokens like {0}, {1} to replace array values
    #-- passed in formatArray
    #---------------------------------------------------------
    def getResponse(self, formatArray):
        index = randint(0, len(self.responses)-1)
        response = [self.responses[index].format(*formatArray)]
        return response