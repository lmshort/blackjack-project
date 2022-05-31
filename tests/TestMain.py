from blackjack_project import __version__
from blackjack_project import Main
import mock
import builtins

class Test:
    """
    Main .py file tests.
    """

    def test_SelectPlayers(Self):
        """
        Test the select players option returns the corresponding integer.
        """
        with mock.patch.object(builtins, 'input', lambda _: '2'):
            assert Main.BlackJackGame.SelectPlayers(Self) == 2

    def test_SelectDeck(Self):
        """
        Test the select players option returns the corresponding integer.
        """
        with mock.patch.object(builtins, 'input', lambda _: '2'):
            assert Main.BlackJackGame.SelectDeck(Self,[]) == 2

    def test_NamePlayers(Self):
        """
        Test the select players option returns the corresponding integer.
        """
        Inputs = ['testname1','testname2']
        with mock.patch.object(builtins, 'input', side_effect=Inputs):
            Players = Main.BlackJackGame.NamePlayers(Self,2)
            assert Players[0].Name == 'testname1'
            assert Players[1].Name == 'testname2'

    """
    StartGame
    """

    """
    PlayersTurn
    """

    """
    DealersTurn
    """

    def test_AssessResults(Self, capfd):
        """
        Assessresults
        """
        class TestPlayer:
            def __init__(Self, Name):
                Self.Name = Name
                Self.Wins = 0
                Self.Ties = 0
                Self.Losses = 0
        
        Players = [TestPlayer("testname1"),TestPlayer("testname2")]
        Scores = {"testname1":[11,21],"testname2":[18],"Dealer":[19]}
        Scores = Main.BlackJackGame.AssessResults(Self, Players,Scores)
        out, err = capfd.readouterr()
        print(len(out))
        for i in out:
            print(i)
        #print(Scores)
        pass

    def test_OverallStandings(Self):
        """
        OverallStandings
        """
        pass

"""
if __name__ == "__main__":
    Test()
"""
