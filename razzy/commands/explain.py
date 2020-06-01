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
        brain = razzy.getBrain()
        word_lists = []
        word_lists.append(["tell", "me", "more"])
        word_lists.append(["go", "on"])
        word_lists.append(["what", "else"])
        isMatch = brain.isMessageListMatch(message, word_lists)

        if isMatch:
            brain.setMemory("explain_continue", True)

        return isMatch

    # ----------------------
    # run
    # ----------------------
    def run(self, message, razzy):
        brain = razzy.getBrain()
        isContinue = brain.getMemory("explain_continue")
        if isContinue:
            message = brain.getMemory("explain_message")
            numSentences = brain.getMemory("explain_message_sentences") * 2
            removeLength = brain.getMemory("explain_message_len")
            brain.setMemory("explain_continue", False)
        else:
            numSentences = 2
            removeLength = 0

        search = self.sanitizeSearch(message)

        brain.setMemory("explain_message", message)

        # Get summary
        summary = wikipedia.summary(search, sentences=numSentences)

        # save request for continuing
        brain.setMemory("explain_message_len", len(summary))
        brain.setMemory("explain_message_sentences", numSentences)

        # remove anything we have already said
        summary = summary[removeLength:]
        # If we still have more to say clean up the response
        if summary:
            summary = unicodedata.normalize('NFKD', summary).encode('ascii', 'ignore')
            summary = summary.decode("utf-8")
        else:
            if isContinue:
                summary = "That is all I know about that"
            else:
                summary = "I don't know anything about that"

        # get CommandResposne
        response = CommandResponse(CommandResponse.CODE_OK, [summary])

        return response

    # ----------------------
    # Remove words we don't want to search for
    # ----------------------
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