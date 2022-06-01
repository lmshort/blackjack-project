from blackjack_project import __version__
from blackjack_project import Objects
import sys


class Test:
    """
    Player Object Tests not required.
    """

    """
    Card Object Tests
    """

    def test_Card(Self):
        """
        test the Objects.Card class initiator and directly called functions work:
            Objects.Class.AssignPicture
            Objects.Class.AssignRank
            Objects.Class.CardValue
        """
        # Testing for an Ace
        Card = Objects.Card(1, "Spade")
        assert Card.Picture == "Ace"
        assert Card.Value == 1
        assert Card.SuitRank == 3

        # Testing for a non-picture value
        Card = Objects.Card(8, "Diamond")
        assert Card.Picture == None
        assert Card.Value == 8
        assert Card.SuitRank == 1

    def test_Describe(Self, capfd):
        """
        tests the Objects.Card.Describe member and ensures output is as expected.
        """
        # Test for a non-picture card
        Objects.Card.Describe(Objects.Card(5, "Club"))
        out, err = capfd.readouterr()
        assert out == "5 of Clubs\n"

        # Test for a picture card
        Objects.Card.Describe(Objects.Card(12, "Heart"))
        out, err = capfd.readouterr()
        assert out == "Queen of Hearts\n"

    """
    Deck/Card Object Tests
    """

    def test_Deck(Self):
        """
        test the Objects.Deck class initiator and Objects.Deck.GenerateDeck member.
        This also tests card object members.
        """
        Deck = Objects.Deck(2)
        assert Deck.NumberOfDecks == 2
        assert len(Deck.Deck) == 2 * 52
        # Test that only 4 pictures exist per suit per deck
        assert sum(Card.Picture != None for Card in Deck.Deck) == 4 * 4 * 2
        # Test that all cards have a suit rank
        assert sum(Card.SuitRank != None for Card in Deck.Deck) == 13 * 4 * 2
        # Test that the corerct amount of a given suit exist
        assert sum(Card.Suit == "Spade" for Card in Deck.Deck) == 13 * 2
        # Test that the total card value is correct
        assert sum(Card.Value for Card in Deck.Deck) == (85) * 4 * 2

    def test_DrawCard(Self):
        """
        tests the Object.Deck.DrawCard member.
        """
        Deck = Objects.Deck(1)
        FirstCardSNumber = Deck.Deck[0].Number
        FirstCardSuit = Deck.Deck[0].Suit
        _, DrawnCard = Objects.Deck.DrawCard(Deck.Deck)
        assert DrawnCard.Number == FirstCardSNumber
        assert DrawnCard.Suit == FirstCardSuit

    """
    Hand Object Tests
    """

    def test_Hand(Self, capfd):
        """
        tests the Object.Hand object and associated measures.
        """
        # Testing hand draw
        Card1 = Objects.Card(2, "Spade")
        Card2 = Objects.Card(12, "Hearts")
        Hand = Objects.Hand.DealHand(Self, Card1, Card2)
        assert len(Hand) == 2

        # Testing card draw (twist/hit)
        Card3 = Objects.Card(1, "Diamond")
        Hand = Objects.Hand.HandTwist(Hand, Card3)
        assert len(Hand) == 3

        # Testing hand value calculation
        assert Objects.Hand.HandValue(Hand) == [13, 23]

        # testing hand value print
        Objects.Hand.PrintHandValue(Hand)
        out, err = capfd.readouterr()
        assert out == "Value: [13]\n"


"""
if __name__ == "__main__":
    Test()
"""
