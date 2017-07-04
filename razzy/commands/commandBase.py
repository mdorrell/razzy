import abc

class CommandBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def run(self, input):
        """Retrieve data from the input source and return an object."""
        return
    
    @abc.abstractmethod
    def getKeywords(self):
        """Return array of keywords."""
        return