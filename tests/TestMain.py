from blackjack_project import __version__
from blackjack_project import Main, Objects
import mock
import builtins
import pytest
from typing import Union
import os


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
        Test the select players option returns the desired values.
        """
        Inputs = ['testname1','testname2']
        with mock.patch.object(builtins, 'input', side_effect=Inputs):
            Players = Main.BlackJackGame.NamePlayers(Self,2)
            assert Players[0].Name == 'testname1'
            assert Players[1].Name == 'testname2'

    """
    StartGame
    """
    # not sure how to test this piece - large function, dependent on many others
    # potentially use fixtures to pre-define the state for each test.

    @pytest.fixture
    def SimulatedSetupDeck(Self) -> Union[object, int, list, dict]:
        Deck = Objects.Deck(1)
        RoundNum = 0
        Players = [Objects.Player(0,'testplayer1'),Objects.Player(1,'testplayer2')]
        Scores = {}
        return Deck, RoundNum, Players, Scores

    def test_PlayersTurn(Self, SimulatedSetupDeck):
        """
        Test the PlayersTurn and dependent UserOptions and BuildHand functions.
        """
        Deck, RoundNum, Players, Scores = SimulatedSetupDeck
        Inputs = ['t','t','t','t','s','t','s']

        # Mocks user inputs and also sets time.sleep to 0 to speed up test.
        with mock.patch.object(builtins, 'input', side_effect=Inputs):
            with mock.patch("time.sleep"):
                Deck, RoundNum, Scores = Main.BlackJackGame.PlayersTurn(Self, Deck.Deck, RoundNum, Players, Scores,)

        assert RoundNum == 1
        assert Scores['testplayer1'] == [8, 18, 18, 28, 18, 28, 28, 38, 18, 28, 28, 38, 28, 38, 38, 48]
        assert Scores['testplayer2'] == [7]
        assert len(Deck) == 43

    def test_DealersTurn(Self, SimulatedSetupDeck):
        """
        Test the DealersTurn function and dependent DealerOptions function.
        """
        Deck, _, _, Scores = SimulatedSetupDeck
        with mock.patch("time.sleep"):
            Deck, Scores = Main.BlackJackGame.DealersTurn(Self, Deck.Deck, Scores)

        assert len(Deck) == 42
        assert Scores['Dealer'][0] == 18

    def test_AssessResults(Self, capfd):
        """
        Test the Assessresults returns the correct winners and losers.
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
        assert out == "Player: testname1 wins!\nPlayer: testname2 loses.\n"

    """
    Overall Standings - print function, unit testing unnecessary
    """

"""
if __name__ == "__main__":
    Test()
"""
