from blackjack_project import __version__
from blackjack_project import functions
import mock
import builtins
import pytest


class Test:
    def test_Iis_positive_integer(Self):
        """
        test the functions.Numeric.is_positive_integer member
        """
        with pytest.raises(Exception):
            assert functions.Numeric.is_positive_integer("-1")

        with pytest.raises(Exception):
            assert functions.Numeric.is_positive_integer("2.5")

    def test_get_user_input_positive_integer(Self):
        """
        test the functions.Logical.get_user_input_positive_integer member
        """
        with mock.patch.object(builtins, "input", lambda _: "4"):
            assert functions.Logical.get_user_input_positive_integer("helloo") == 4

        with mock.patch.object(builtins, "input", lambda _: "a"):
            assert functions.Logical.get_user_input_positive_integer("helloo") == False

        with mock.patch.object(builtins, "input", lambda _: "-1"):
            assert functions.Logical.get_user_input_positive_integer("helloo") == False

    def test_get_user_input_string(Self):
        """
        test the functions.get_user_input_string member
        """
        with mock.patch.object(builtins, "input", lambda _: "ab"):
            assert functions.Logical.get_user_input_string("helloo") == "ab"

    def test_is_string_longer_than_equal_to(Self):
        """
        test the functions.Logical.is_string_longer_than_equal_to member
        """
        assert functions.Logical.is_string_longer_than_equal_to("string", 1) == True
        assert functions.Logical.is_string_longer_than_equal_to("string", 6) == True
        assert functions.Logical.is_string_longer_than_equal_to("string", 10) == False

    def test_validate_name(Self):
        """
        test the functions.Logical.validate_name member.
        """
        assert functions.Logical.validate_name("string") == True

    def test_randomise(Self):
        """
        test the functions.Logical.randomise member.
        """
        # Pseudo-randomness test
        test_data = list(range(1, 100))
        assert functions.Logical.randomise(test_data) != test_data

    def test_shift_player_order(Self):
        """
        test the functions.Logical.shift_player_order member.
        """
        # Pseudo-randomness test
        test_data = [0, 1, 2, 3]
        assert functions.Logical.shift_player_order(test_data) == [3, 0, 1, 2]

    def test_get_stick_or_twist_input(Self):
        """
        test the functions.Logical.get_stick_or_twist_input member.
        """
        with mock.patch.object(builtins, "input", lambda _: "s"):
            assert functions.Logical.get_stick_or_twist_input() == "stick"

        with mock.patch.object(builtins, "input", lambda _: "t"):
            assert functions.Logical.get_stick_or_twist_input() == "twist"

    def test_get_player_name(Self):
        """
        test the functions.Logical.get_player_name member.
        """
        with mock.patch.object(builtins, "input", lambda _: "Name"):
            assert functions.Logical.get_player_name(1) == "Name"


"""
if __name__ == "__main__":
    Test()
"""
