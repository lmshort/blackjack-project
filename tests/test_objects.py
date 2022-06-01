from blackjack_project import __version__
from blackjack_project import objects
import sys


class Test:
    """
    Player Object Tests not required.
    """

    """
    Card Object Tests
    """

    def test_card(self):
        """
        test the objects.Card class initiator and directly called functions work:
            objects.Class.AssignPicture
            objects.Class.AssignRank
            objects.Class.CardValue
        """
        # Testing for an Ace
        card = objects.Card(1, "Spade")
        assert card.picture == "Ace"
        assert card.value == 1
        assert card.suit_rank == 3

        # Testing for a non-picture value
        card = objects.Card(8, "Diamond")
        assert card.picture == None
        assert card.value == 8
        assert card.suit_rank == 1

    def test_describe(self, capfd):
        """
        tests the objects.Card.describe member and ensures output is as expected.
        """
        # Test for a non-picture card
        objects.Card.describe(objects.Card(5, "Club"))
        out, err = capfd.readouterr()
        assert out == "5 of Clubs\n"

        # Test for a picture card
        objects.Card.describe(objects.Card(12, "Heart"))
        out, err = capfd.readouterr()
        assert out == "Queen of Hearts\n"

    """
    Deck/Card Object Tests
    """

    def test_deck(self):
        """
        test the objects.Deck class initiator and objects.Deck.GenerateDeck member.
        This also tests card object members.
        """
        deck = objects.Deck(2)
        assert deck.number_of_decks == 2
        assert len(deck.deck) == 2 * 52
        # Test that only 4 pictures exist per suit per deck
        assert sum(card.picture != None for card in deck.deck) == 4 * 4 * 2
        # Test that all cards have a suit rank
        assert sum(card.suit_rank != None for card in deck.deck) == 13 * 4 * 2
        # Test that the corerct amount of a given suit exist
        assert sum(card.suit == "Spade" for card in deck.deck) == 13 * 2
        # Test that the total card value is correct
        assert sum(card.value for card in deck.deck) == (85) * 4 * 2

    def test_draw_card(self):
        """
        tests the Object.Deck.DrawCard member.
        """
        deck = objects.Deck(1)
        first_cards_number = deck.deck[0].number
        first_cards_suit = deck.deck[0].suit
        _, drawn_card = objects.Deck.draw_card(deck.deck)
        assert drawn_card.number == first_cards_number
        assert drawn_card.suit == first_cards_suit

    """
    Hand Object Tests
    """

    def test_hand(self, capfd):
        """
        tests the Object.Hand object and associated measures.
        """
        # Testing hand draw
        card_1 = objects.Card(2, "Spade")
        card_2 = objects.Card(12, "Hearts")
        hand = objects.Hand.deal_hand(self, card_1, card_2)
        assert len(hand) == 2

        # Testing card draw (twist/hit)
        card_3 = objects.Card(1, "Diamond")
        hand = objects.Hand.hand_twist(hand, card_3)
        assert len(hand) == 3

        # Testing hand value calculation
        assert objects.Hand.hand_value(hand) == [13, 23]

        # testing hand value print
        objects.Hand.print_hand_value(hand)
        out, err = capfd.readouterr()
        assert out == "Value: [13]\n"


"""
if __name__ == "__main__":
    Test()
"""
