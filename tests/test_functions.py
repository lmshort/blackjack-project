from blackjack_project import __version__
from blackjack_project import functions
import mock
import builtins
import pytest


class Test:
    def test_is_positive_integer_negative_value(Self):
        """
        Test the functions.Numeric.is_positive_integer member with a negative integer
        """
        with pytest.raises(Exception):
            assert functions.Numeric.is_positive_integer("-1")

    def test_is_positive_integer_decimal(Self):
        """
        Test the functions.Numeric.is_positive_integer member with a non-integer
        """
        with pytest.raises(Exception):
            assert functions.Numeric.is_positive_integer("2.5")

    def test_get_user_input_positive_integer(Self):
        """
        Test the functions.Logical.get_user_input_positive_integer member with correct and incorrect values
        """
        inputs = ["4", "a"]
        with mock.patch.object(builtins, "input", side_effect=inputs):
            assert (
                functions.Logical.get_user_input_positive_integer("helloo"),
                functions.Logical.get_user_input_positive_integer("helloo"),
            ) == (4, False)

    def test_get_user_input_string(Self):
        """
        Test the functions.get_user_input_string member
        """
        with mock.patch.object(builtins, "input", lambda _: "ab"):
            assert functions.Logical.get_user_input_string("helloo") == "ab"

    def test_is_string_longer_than_equal_to(Self):
        """
        Test the functions.Logical.is_string_longer_than_equal_to member
        """
        assert (
            functions.Logical.is_string_longer_than_equal_to("string", 1),
            functions.Logical.is_string_longer_than_equal_to("string", 6),
            functions.Logical.is_string_longer_than_equal_to("string", 10),
        ) == (True, True, False)

    def test_validate_name(Self):
        """
        Test the functions.Logical.validate_name member.
        """
        assert functions.Logical.validate_name("string") == True

    def test_randomise(Self):
        """
        Test the functions.Logical.randomise member.
        """
        # Pseudo-randomness test
        test_data = list(range(1, 100))
        assert functions.Logical.randomise(test_data) != test_data

    def test_shift_player_order(Self):
        """
        Test the functions.Logical.shift_player_order member.
        """
        # Pseudo-randomness test
        test_data = [0, 1, 2, 3]
        assert functions.Logical.shift_player_order(test_data) == [3, 0, 1, 2]

    def test_get_stick_or_twist_input_stick(Self):
        """
        Test the functions.Logical.get_stick_or_twist_input member with a stick input.
        """
        with mock.patch.object(builtins, "input", lambda _: "s"):
            assert functions.Logical.get_stick_or_twist_input() == "stick"

    def test_get_stick_or_twist_input_twist(Self):
        """
        Test the functions.Logical.get_stick_or_twist_input member with a twist input.
        """
        with mock.patch.object(builtins, "input", lambda _: "t"):
            assert functions.Logical.get_stick_or_twist_input() == "twist"

    def test_get_player_name(Self):
        """
        Test the functions.Logical.get_player_name member.
        """
        with mock.patch.object(builtins, "input", lambda _: "Name"):
            assert functions.Logical.get_player_name(1) == "Name"


"""
if __name__ == "__main__":
    Test()
"""
