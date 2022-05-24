import random
import time

class Numeric:
    """
    Numeric functions supporting calculative operations.
    """
    def IsPositiveInteger(value: str):
        """
        TBC
        """
        return value.isdigit()
    
    def CountInNewHand():
        """
        TBC
        """
        t = 5
        print("\nStarting new hand...")
        while t >= 1:
            time.sleep(1)
            print(t)
            t -= 1


class Logical:
    """
    Logical, user input and object manipulation supporting game machinations.
    """

    def GetUserInputPostitiveInteger(Prompt: str) -> int:
        """
        TBC
        """
        value = input("\n" + str(Prompt) + " [1-5]:")
        if Numeric.IsPositiveInteger(value):
            if int(value) <= 5:
                return int(value)
        else:
            return False

    def GetUserInputString(Prompt: str) -> str:
        """
        TBC
        """
        return str(input("\n" + str(Prompt) + ":\n"))

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

    def GetStickOrTwistInput():
        result = None
        while result == None:
            value = input(f"Stick (enter 's') or Twist (enter 't') ?:")
            try:
                if len(value) == 1 and value.lower() in ('s'):
                    result = "stick"
                    return result
                elif len(value) != 0 and value.lower() in ('t'):
                    result = "twist"
                    return result
                else: raise
            except:
                print("Error - Please ensure correct text syntax used.")
                
    def GetPlayerName(self, PlayerID: int) -> str:
        """_Summary_

        """
        while True:
            PlayerName = Logical.GetUserInputString("Enter player " + str(PlayerID) + " name")
            if Logical.ValidateName(PlayerName):
                return str(PlayerName)
            print("Error - Incorrect name format (remember: must be > 1 character)")



if __name__ == "__main__":
    pass
