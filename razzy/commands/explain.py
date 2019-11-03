import wikipedia
import unicodedata

from commandBase import CommandBase
from commandResponse import CommandResponse


class Explain(CommandBase):
    # Words we remove from the search
    removeList = ["Razzy"]

    @staticmethod
    def getKeywords(self):
        keywords = []
        keywords.append(["tell", "me", "about"])
        keywords.append(["explain"])
        keywords.append(["who", "is"])
        keywords.append(["what", "is"])
        return keywords


    # ----------------------
    # doContinue
    # ----------------------
    def doContinue(self, message, razzy):
        return False

    def run(self, message, razzy):
        search = self.sanitizeSearch(message)

        response = wikipedia.summary(search, sentences=2)
        response = unicodedata.normalize('NFKD', response).encode('ascii', 'ignore')
        response = response.decode("utf-8")

        response = CommandResponse(CommandResponse.CODE_OK, [response]);
        return response

    def sanitizeSearch(self, message):

        # remove words in keywords from search
        wordList = message.split()
        removeList = self.getKeywords(self)
        removeList.append(self.removeList)
        for row in removeList:
            for word in row:
                if word in wordList:
                    wordList.remove(word)

        # Other words we want to remove
        if word in wordList:
            wordList.remove("Razzy")

        search = ' '.join(wordList)

        return search