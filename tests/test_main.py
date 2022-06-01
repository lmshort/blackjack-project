from blackjack_project import __version__, main
from blackjack_project import objects
import mock
import builtins
import pytest
from typing import Union


class Test:
    """
    Main .py file tests.
    """

    def test_select_players(self):
        """
        Test the select players option returns the corresponding integer.
        """
        with mock.patch.object(builtins, "input", lambda _: "2"):
            assert main.BlackjackGame.select_players(self) == 2

    def test_select_deck(self):
        """
        Test the select players option returns the corresponding integer.
        """
        with mock.patch.object(builtins, "input", lambda _: "2"):
            assert main.BlackjackGame.select_deck(self, []) == 2

    def test_name_players(self):
        """
        Test the select players option returns the desired values.
        """
        inputs = ["testname1", "testname2"]
        with mock.patch.object(builtins, "input", side_effect=inputs):
            players = main.BlackjackGame.name_players(2)
            assert players[0].name == "testname1"
            assert players[1].name == "testname2"

    """
    StartGame
    """
    # not sure how to test this piece - large function, dependent on many others
    # potentially use fixtures to pre-define the state for each test.

    @pytest.fixture
    def simulated_setup_deck(self) -> Union[object, int, list, dict]:
        deck = objects.Deck(1)
        round_num = 0
        players = [objects.Player(0, "testplayer1"), objects.Player(1, "testplayer2")]
        scores = {}
        return deck, round_num, players, scores

    def test_players_turn(self, simulated_setup_deck):
        """
        Test the players_turn and dependent UserOptions and BuildHand `func`tions.
        """
        deck, round_num, players, scores = simulated_setup_deck
        inputs = ["t", "t", "t", "t", "s", "t", "s"]

        # Mocks user inputs and also sets time.sleep to 0 to speed up test.
        with mock.patch.object(builtins, "input", side_effect=inputs):
            with mock.patch("time.sleep"):
                deck, round_num, scores = main.BlackjackGame.players_turn(
                    self,
                    deck.deck,
                    round_num,
                    players,
                    scores,
                )

        assert round_num == 1
        assert scores["testplayer1"] == [
            8,
            18,
            18,
            28,
            18,
            28,
            28,
            38,
            18,
            28,
            28,
            38,
            28,
            38,
            38,
            48,
        ]
        assert scores["testplayer2"] == [7]
        assert len(deck) == 43

    def test_dealers_turn(self, simulated_setup_deck):
        """
        Test the dealers_turn function and dependent DealerOptions function.
        """
        deck, _, _, scores = simulated_setup_deck
        with mock.patch("time.sleep"):
            deck, scores = main.BlackjackGame.dealers_turn(self, deck.deck, scores)

        assert len(deck) == 42
        assert scores["Dealer"][0] == 18

    def test_assess_results(self, capfd):
        """
        Test the assess_results returns the correct winners and losers.
        """

        class TestPlayer:
            def __init__(self, name):
                self.name = name
                self.wins = 0
                self.ties = 0
                self.losses = 0

        players = [TestPlayer("testname1"), TestPlayer("testname2")]
        scores = {"testname1": [11, 21], "testname2": [18], "Dealer": [19]}
        scores = main.BlackjackGame.assess_results(players, scores)
        out, err = capfd.readouterr()
        assert out == "Player: testname1 wins!\nPlayer: testname2 loses.\n"

    """
    Overall Standings - print function, unit testing unnecessary
    """


"""
if __name__ == "__main__":
    Test()
"""
