from blackjack_project import __version__
from blackjack_project import Functions
import mock
import builtins
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
        test the Functions.Logical.ValidateName member.
        """
        assert Functions.Logical.ValidateName("string") == True

    def test_Randomise(Self):
        """
        test the Functions.Logical.Randomise member.
        """
        # Pseudo-randomness test
        TestData = list(range(1, 100))
        assert Functions.Logical.Randomise(TestData) != TestData

    def test_ShiftPlayerOrder(Self):
        """
        test the Functions.Logical.ShiftPlayerOrder member.
        """
        # Pseudo-randomness test
        TestData = [0,1,2,3]
        assert Functions.Logical.ShiftPlayerOrder(TestData) == [3,0,1,2]

    def test_GetStickOrTwistInput(Self):
        """
        test the Functions.Logical.GetStickOrTwistInput member.
        """
        with mock.patch.object(builtins, 'input', lambda _: 's'):
            assert Functions.Logical.GetStickOrTwistInput() == 'stick'

        with mock.patch.object(builtins, 'input', lambda _: 't'):
            assert Functions.Logical.GetStickOrTwistInput() == 'twist'

    def test_GetPlayerName(Self):
        """
        test the Functions.Logical.GetPlayerName member.
        """
        with mock.patch.object(builtins, 'input', lambda _: 'Name'):
            assert Functions.Logical.GetPlayerName(1) == 'Name'


"""
if __name__ == "__main__":
    Test()
"""
