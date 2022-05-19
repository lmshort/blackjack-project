from blackjack_project import __version__
from blackjack_project import Functions
import pytest
import sys
import mock
import builtins

class Test:
    def test_Version(Self):
        """
        Dummmy placeholder test
        """
        assert __version__ == '0.1.0'

    def test_IsPositiveInteger(Self):
        """
        test the Functions.Numeric.IsPositiveInteger member
        """
        with pytest.raises(Exception):
            assert Functions.Numeric.IsPositiveInteger("-1")

        with pytest.raises(Exception):
            assert Functions.Numeric.IsPositiveInteger("2.5")
            
    def test_GetUserInputPostitiveInteger(Self):
        """
        test the Functions.Logical.GetUserInputPositiveInteger member
        """
        with mock.patch.object(builtins, 'input', lambda _: '23'):
            assert Functions.Logical.GetUserInputPostitiveInteger("helloo") == 23

        with mock.patch.object(builtins, 'input', lambda _: 'a'):
            assert Functions.Logical.GetUserInputPostitiveInteger("helloo") == False

        with mock.patch.object(builtins, 'input', lambda _: '-1'):
            assert Functions.Logical.GetUserInputPostitiveInteger("helloo") == False



"""
if __name__ == "__main__":
    Test()
"""

