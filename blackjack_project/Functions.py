"""
TBC
"""
import random

class Numeric:
    """
    Numeric functions supporting calculative operations.
    """
    def IsPositiveInteger(value: str):
        """
        TBC
        """
        return value.isdigit()



class Logical:
    """
    Logical, user input and object manipulation supporting game machinations.
    """

    def GetUserInputPostitiveInteger(Prompt: str) -> int:
        """
        TBC
        """
        value = input("\n" + str(Prompt) + " [1-999..]:")
        if Numeric.IsPositiveInteger(value):
            return int(value)
        else:
            return False

    def GetUserInputString(Prompt: str) -> str:
        """
        TBC
        """
        return str(input("\n" + str(Prompt) + ":\n"))

    def NamePlayer(PlayerID: int, PlayerName: str):
        """
        TBC
        """
        print("Setting player " + str(PlayerID) + " name to " + str(PlayerName))

    def IsStringLongerThanEqualTo(String: str, Length: int) -> bool:
        """
        TBC
        """
        return len(String) >= Length

    def ValidateName(String: str) -> bool:
        """
        TBC
        """
        if Logical.IsStringLongerThanEqualTo(String,1):
            return True
        else:
            return False

    def Randomise(Deck: object):
        return random.sample(Deck,len(Deck))

    def ShiftPlayerOrder(List: list):
        return List[-1:] + List[:-1] 



if __name__ == "__main__":
    pass
