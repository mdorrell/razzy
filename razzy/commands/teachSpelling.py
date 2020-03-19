import unicodedata

from commandBase import CommandBase
from commandResponse import CommandResponse


class TeachSpelling(CommandBase):

    currentState = "ask"

    currentWord  = "hamburger"

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
    # doContinueCommand
    # ----------------------
    def doContinueCommand(self):
        """Return boolean when the command will continue"""
        return True

    def run(self, message, razzy):
        print("spelling " + message)

        if (self.currentState == "ask"):
            message = ["How do you spell " + self.currentWord]
            self.currentState = "answer"
        else:
            message = ["You said " + message]
            self.currentState = "ask"

        response = CommandResponse(CommandResponse.CODE_OK, message);
        return response