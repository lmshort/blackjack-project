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

    def test_card_ace(self):
        """
        test the objects.Card class initiator and directly called functions work:
            objects.Class.AssignPicture
            objects.Class.AssignRank
            objects.Class.CardValue
        for an ace card.
        """
        # Testing for an Ace
        card = objects.Card(1, "Spade")
        assert (card.picture, card.value, card.suit_rank) == ("Ace", 1, 3)

    def test_card_number(self):
        """
        test the objects.Card class initiator and directly called functions work:
            objects.Class.AssignPicture
            objects.Class.AssignRank
            objects.Class.CardValue
        for a non-picture card.
        """
        # Testing for a non-picture value
        card = objects.Card(8, "Diamond")
        assert (card.picture, card.value, card.suit_rank) == (None, 8, 1)

    def test_describe_number(self, capfd):
        """
        tests the objects.Card.describe member and ensures output is as expected for a non-picture card.
        """
        # Test for a non-picture card
        objects.Card.describe(objects.Card(5, "Club"))
        out, err = capfd.readouterr()
        assert out == "5 of Clubs\n"

    def test_describe_picture(self, capfd):
        """
        tests the objects.Card.describe member and ensures output is as expected for a picture card.
        """
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
        assert (
            deck.number_of_decks,
            len(deck.deck),
            sum(card.picture != None for card in deck.deck),
            sum(card.suit_rank != None for card in deck.deck),
            sum(card.suit == "Spade" for card in deck.deck),
            sum(card.value for card in deck.deck),
        ) == (2, 2 * 52, 4 * 4 * 2, 13 * 4 * 2, 13 * 2, (85) * 4 * 2)

    def test_draw_card(self):
        """
        tests the Object.Deck.DrawCard member.
        """
        deck = objects.Deck(1)
        first_cards_number = deck.deck[0].number
        first_cards_suit = deck.deck[0].suit
        _, drawn_card = objects.Deck.draw_card(deck.deck)
        assert (drawn_card.number, drawn_card.suit) == (
            first_cards_number,
            first_cards_suit,
        )

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

        # Testing card draw (twist/hit)
        card_3 = objects.Card(1, "Diamond")
        hand = objects.Hand.hand_twist(hand, card_3)

        # testing hand value print
        objects.Hand.print_hand_value(hand)
        out, err = capfd.readouterr()

        assert (len(hand), objects.Hand.hand_value(hand), out) == (
            3,
            [13, 23],
            "Value: [13]\n",
        )


"""
if __name__ == "__main__":
    Test()
"""
