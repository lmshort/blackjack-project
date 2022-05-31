import random
import time

class Numeric:
    """
    Numeric functions supporting calculative operations.
    """
    def IsPositiveInteger(value: str) -> bool:
        """_summary_
        Confirms whether a received string value is a positive integer.

        Args:
            value (str): string variable containing suspected positive integer value

        Returns:
            bool: boolean state confirming whether string represents a positive integer.
        """
        return value.isdigit()
    
    def CountInNewHand():
        """
        _summary_
        Executes a 5 second countdown - used to transition between interfaces.
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
        """_summary_
        Prompts the user for a positive integer input.

        Args:
            Prompt (str): prompt message.

        Returns:
            int: value returned from user.
        """
        value = input("\n" + str(Prompt) + " [1-5]:")
        if Numeric.IsPositiveInteger(value):
            if int(value) <= 5:
                return int(value)
        else:
            return False

    def GetUserInputString(Prompt: str) -> str:
        """_summary_
        Prompts the user for a string input.

        Args:
            Prompt (str): prompt message.

        Returns:
            str: string value returned from user.
        """
        return str(input("\n" + str(Prompt) + ":\n"))

    def IsStringLongerThanEqualTo(String: str, Length: int) -> bool:
        """_summary_
        Simple logic to confirm if a string is longer than or equal to a given value.

        Args:
            String (str): String to check
            Length (int): no. characters integer value to check against.

        Returns:
            bool: state - true if longer than equal to given value.
        """
        return len(String) >= Length

    def ValidateName(String: str) -> bool:
        """_summary_
        Validates whether a string meets a given length condition.

        Args:
            String (str): String to check

        Returns:
            bool: state - true if meets condition
        """
        if Logical.IsStringLongerThanEqualTo(String,1):
            return True
        else:
            return False

    def Randomise(Deck: list) -> list:
        """_summary_
        Randomises order of a list, simulating a shuffle operation

        Args:
            Deck (list): List of items
        Returns:
            list: shuffled list
        """
        return random.sample(Deck,len(Deck))

    def ShiftPlayerOrder(List: list) -> list:
        """_summary_
        Pushes the top element of a list to the bottom.

        Args:
            List (list): list of players.

        Returns:
            list: list of players
        """
        return List[-1:] + List[:-1] 

    def GetStickOrTwistInput() -> str:
        """_summary_
        Prompts user to enter either "stick" or "twist".

        Returns:
            str: string decision (either stick or twist)
        """
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
                
    def GetPlayerName(PlayerID: int) -> str:
        """_Summary_
        Prompts the user to enter a player name string.

        Returns:
            str: playername
        """
        while True:
            PlayerName = Logical.GetUserInputString("Enter player " + str(PlayerID) + " name")
            if Logical.ValidateName(PlayerName):
                return str(PlayerName)
            print("Error - Incorrect name format (remember: must be > 1 character)")


if __name__ == "__main__":
    pass
