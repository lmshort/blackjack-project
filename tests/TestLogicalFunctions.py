from blackjack_project import __version__
from blackjack_project import Functions
import pytest
import mock
import builtins

class Test:
    def test_Version(Self):
        """
        Dummmy placeholder test
        """
        assert __version__ == '0.1.0'
            
    def test_GetUserInputPostitiveInteger(Self):
        """
        test the Functions.Logical.GetUserInputPositiveInteger member
        """
        with mock.patch.object(builtins, 'input', lambda _: '4'):
            assert Functions.Logical.GetUserInputPostitiveInteger("helloo") == 4

        with mock.patch.object(builtins, 'input', lambda _: 'a'):
            assert Functions.Logical.GetUserInputPostitiveInteger("helloo") == False

        with mock.patch.object(builtins, 'input', lambda _: '-1'):
            assert Functions.Logical.GetUserInputPostitiveInteger("helloo") == False

    def test_GetUserInputString(Self):
        """
        test the Functions.Logical.GetUserInputString member
        """
        with mock.patch.object(builtins, 'input', lambda _: 'ab'):
            assert Functions.Logical.GetUserInputString("helloo") == 'ab'
        
    def test_IsStringLongerThanEqualTo(Self):
        """
        test the Functions.Logical.IsStringLongerThanEqualTo member
        """
        assert Functions.Logical.IsStringLongerThanEqualTo("string", 1) == True
        assert Functions.Logical.IsStringLongerThanEqualTo("string", 6) == True
        assert Functions.Logical.IsStringLongerThanEqualTo("string", 10) == False

    def test_ValidateName(Self):
        """
        test the Functions.Logical.ValidateName member
        """
        assert Functions.Logical.ValidateName("string") == True




"""
if __name__ == "__main__":
    Test()
"""

