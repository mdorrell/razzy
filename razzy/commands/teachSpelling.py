import unicodedata
import random

from commandBase import CommandBase
from commandResponse import CommandResponse


class TeachSpelling(CommandBase):

    currentState = "ask"

    wordList = [
        "boy",
        "soon",
        "came",
        "want",
        "eggs",
        "nurse",
        "curve",
        "turn",
        "burn",
        "curl",
        "purse",
        "growth",
        "affect",
        "fish",
        "mammal",
        "fruit"
    ]

    @staticmethod
    def getKeywords(self):
        keywords = []
        keywords.append(["teach", "spelling"])
        keywords.append(["review", "spelling"])
        keywords.append(["teach", "spell"])
        keywords.append(["practice", "spelling"])
        return keywords


    # ----------------------
    # doContinue
    # ----------------------
    def doContinue(self, message, razzy):
        return True

    # ----------------------
    # Run command
    # ----------------------
    def run(self, message, razzy):
        print("spelling " + message)
        brain = razzy.getBrain()
        currentWord = brain.getMemory('currentWord')
        print("current word = " + currentWord)

        # if there is a current word, see if it was spelled right
        if (currentWord):

            # clean up message to make it match more
            message = message.replace(" ", "").lower()

            # if they are correct
            if (message == currentWord):
                message = ["Yes, you are correct"]
            else:
                message = ["No, you are wrong."]
                correctSpelling = self.getCorrectSpelling(currentWord)
                print("Correct = " + correctSpelling)
                message.append("The correct way to spell " + currentWord + " is " + correctSpelling)

            currentWord = self.getRandomWord(brain)
            message.append("How do you spell " + currentWord)

        # otherwise ask a new word
        else:
            currentWord = self.getRandomWord(brain)
            message = ["How do you spell " + currentWord]

        response = CommandResponse(CommandResponse.CODE_OK, message);
        return response

    # ----------------------
    # Get a random word from the word list
    # ----------------------
    def getRandomWord(self, brain):
        index = random.randint(1, len(self.wordList) - 1)
        currentWord = self.wordList[index]
        brain.setMemory('currentWord', currentWord)

        return currentWord

    # ----------------------
    # Get the correct spelling of the word
    # ----------------------
    def getCorrectSpelling(self, currentWord):
        spellingWord = "";
        for letter in currentWord:
            spellingWord += letter + ", "
        return spellingWord.strip()
