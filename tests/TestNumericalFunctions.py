from blackjack_project import __version__
from blackjack_project import Functions
import pytest

class Test:
    def test_IsPositiveInteger(Self):
        """
        test the Functions.Numeric.IsPositiveInteger member
        """
        with pytest.raises(Exception):
            assert Functions.Numeric.IsPositiveInteger("-1")

        with pytest.raises(Exception):
            assert Functions.Numeric.IsPositiveInteger("2.5")


"""
if __name__ == "__main__":
    Test()
"""
