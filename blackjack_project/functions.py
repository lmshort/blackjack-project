"""
Functions file - contains some simple, reusable functions.
"""
import random
import time


class Numeric:
    """
    Numeric functions supporting calculative operations.
    """

    def is_positive_integer(value: str) -> bool:
        """Confirms whether a received string value is a positive integer.

        Args:
            value (str): string variable containing suspected positive integer value

        Returns:
            bool: boolean state confirming whether string represents a positive integer.
        """
        return value.isdigit()

    def count_in_new_hand():
        """Executes a 5 second countdown - used to transition between interfaces."""
        time_value = 5
        print("\nStarting new hand...")
        while time_value >= 1:
            time.sleep(1)
            print(time_value)
            time_value -= 1


class Logical:
    """
    Logical, user input and object manipulation supporting game machinations.
    """

    def get_user_input_positive_integer(prompt: str) -> int:
        """Prompts the user for a positive integer input.

        Args:
            prompt (str): prompt message.

        Returns:
            int: value returned from user.
        """
        value = input("\n" + str(prompt) + " [1-5]:")
        if Numeric.is_positive_integer(value):
            if int(value) <= 5:
                return int(value)
        else:
            return False

    def get_user_input_string(prompt: str) -> str:
        """Prompts the user for a string input.

        Args:
            prompt (str): prompt message.

        Returns:
            str: string value returned from user.
        """
        return str(input("\n" + str(prompt) + ":\n"))

    def is_string_longer_than_equal_to(string: str, length: int) -> bool:
        """Simple logic to confirm if a string is longer than or equal to a given value.

        Args:
            string (str): String to check
            length (int): no. characters integer value to check against.

        Returns:
            bool: state - true if longer than equal to given value.
        """
        return len(string) >= length

    def validate_name(string: str) -> bool:
        """Validates whether a string meets a given length condition.

        Args:
            string (str): String to check

        Returns:
            bool: state - true if meets condition
        """
        return bool(Logical.is_string_longer_than_equal_to(string, 1))

    def randomise(deck: list) -> list:
        """Randomises order of a list, simulating a shuffle operation

        Args:
            deck (list): List of items
        Returns:
            list: shuffled list
        """
        return random.sample(deck, len(deck))

    def shift_player_order(list: list) -> list:
        """Pushes the top element of a list to the bottom.

        Args:
            list (list): list of players.

        Returns:
            list: list of players
        """
        return list[-1:] + list[:-1]

    def get_stick_or_twist_input() -> str:
        """Prompts user to enter either "stick" or "twist".

        Returns:
            str: string decision (either stick or twist)
        """
        result = None
        while result is None:
            value = input("Stick (enter 's') or Twist (enter 't') ?:")
            try:
                if len(value) == 1 and value.lower() in ("s"):
                    result = "stick"
                    return result
                if len(value) != 0 and value.lower() in ("t"):
                    result = "twist"
                    return result
                raise None
            except:
                print("Error - Please ensure correct text syntax used.")

    def get_player_name(player_id: int) -> str:
        """Prompts the user to enter a player name string.

        Returns:
            str: playername
        """
        while True:
            player_name = Logical.get_user_input_string(
                "Enter player " + str(player_id) + " name"
            )
            if Logical.validate_name(player_name):
                return str(player_name)
            print("Error - Incorrect name format (remember: must be > 1 character)")


if __name__ == "__main__":
    pass
