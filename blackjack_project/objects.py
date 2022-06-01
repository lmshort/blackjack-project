"""
Objects file - contains BlackJackGame object definitons.
"""
from typing import Union


class Player:
    """
    Player class - created for each player added to the game, contains overall information and stats.
    """

    def __init__(self, player_id: int, player_name: str):
        """Player class initiated with overall information and stats.

        Args:
            self (object): Player object
            player_id (int): Simple integer used to account for differences when PlayerName is duplicately used.
            player_name (str): Player name string
        """
        self.id = player_id
        self.name = player_name
        # self.Money = 100
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.hand = None


class Deck:
    """
    Deck class - a class container where list of Card objects are stored.
    """

    def __init__(self, number_of_decks: int):
        """Deck class initiated with no. decks and deck attribute, a list of cards.

        Args:
            self (object): Deck object
            number_of_decks (int): Number of decks to be used
        """
        self.number_of_decks = number_of_decks
        self.deck = Deck.generate_deck(number_of_decks)
        # include cards and suits

    def generate_deck(number_of_decks: int) -> list:
        """Generate the deck from card objects, based on specified number of decks.

        Args:
            number_of_decks (int): Number of decks to be used

        Returns:
            list: list of card objects representing a deck
        """
        deckList = []
        for _ in range(0, number_of_decks):
            for j in range(1, 14):
                for k in ("Diamond", "Heart", "Spade", "Club"):
                    deckList.append(Card(j, k))
        return deckList

    def draw_card(self) -> Union[object, object]:
        """Draws a card from a deck.

        Args:
            self (list): Deck Deck attribute (represents a list of cards)

        Returns:
            object: Deck Deck attribute (list of cards)
            object: Card object, representing the drawn card/
        """
        drawn_card = self.pop(0)
        return self, drawn_card

    def count_cards_in_deck(self) -> int:
        """Count the number of cards in a deck

        Args:
            self (list): Deck Deck attribute (represents a list of cards)

        Returns:
            int: number of cards left in the deck
        """
        return len(self)


class Card:
    """
    Card class - card represents a single game card, with real-life attributes assigned.
    """

    def __init__(self, card_number: int, card_suit: str):
        """Initiator function defines key attributes for a card.

        Args:
            self (object): card object
            card_number (int): card number - ranges from 1-13
            card_suit (str): string suit classification (4 options)
        """
        self.number = card_number
        self.picture = Card.assign_picture(card_number)
        self.suit = card_suit
        self.suit_rank = Card.assign_rank(card_suit)
        self.value = Card.card_value(card_number)

    def assign_picture(card_number: int) -> str:
        """Assigns a picture attribute, based on card number.

        Args:
            card_number (int): card number assigned.

        Returns:
            str: textual description of the card, should it be a "picture" card
        """
        picture_options = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if card_number in picture_options:
            return picture_options[card_number]

    def assign_rank(suit: str) -> int:
        """Assigns a rank, based on its given suit.

        Args:
            suit (str): given card suit

        Returns:
            int: ranking, based on suit (1 -> 4)
        """
        rank_options = {"Diamond": 1, "Heart": 2, "Spade": 3, "Club": 4}
        if suit in rank_options:
            return rank_options[suit]

    def describe(self):
        """Prints a description of a given card.

        Args:
            self (object): card object
        """
        if self.number not in (1, 11, 12, 13):
            print(f"{self.number} of {self.suit}s")
        elif self.number in (1, 11, 12, 13):
            print(f"{self.picture} of {self.suit}s")

    def card_value(card_number: int) -> int:
        """Returns the card value

        Args:
            self (object): card object
            card_number (int): _description_

        Returns:
            int: _description_
        """
        if card_number > 10:
            card_value = 10
        else:
            card_value = card_number
        return card_value


class Hand:
    """
    Hand class represents a player's collection of cards.
    """

    def __init__(self):
        """Initiator function defines the hand attribute "Hand" - a list of cards, based on initial 2 card draw.

        Args:
            self (object): Hand object
        """
        self.hand = None  # Hand.DealHand(self,Card1, Card2)

    def deal_hand(self, drawn_card_1: object, drawn_card_2: object) -> list:
        """Function deals a hand, creating a list of card objects for an initial deal.

        Args:
            self (object): Hand object
            drawn_card_1 (object): Drawn card 1
            drawn_card_2 (object): Drawn card 2

        Returns:
            object: Hand hand attribute, a list of cards.
        """
        self.hand = [drawn_card_1, drawn_card_2]
        return self.hand

    def hand_twist(self, card: object) -> list:
        """Draws a single card.

        Args:
            self (list): Hand Hand attribute - list of cards
            card (object): Drawn card

        Returns:
            list: Hand Hand attribute - list of cards
        """
        self.append(card)
        return self

    def hand_value(self) -> list:
        """Determines potential hand values, based on cards in hand.

        Args:
            self (list): Hand Hand attribute - list of cards

        Returns:
            list: List of possible values, based on card combinations
        """
        # Initiate array with a 0 value.
        total_values = [0]
        for card in self:
            # If not an "ace" card, value is added to each array element.
            if card.value != 1:
                total_values = [x + card.value for x in total_values]
            # If an "ace" card, additional combinations possible, each accounted for.
            else:
                total_values_previous = total_values
                total_values = [x + 1 for x in total_values]
                for value in total_values_previous:
                    total_values.append(value + 11)
        return total_values

    def print_hand_value(self):
        """Prints the hand card value.

        Args:
            self (list): Hand Hand attribute - a list of cards
        """
        total_values = Hand.hand_value(self)
        if all(Value > 21 for Value in total_values):
            print("BUST!")
        else:
            # Just returns the values which satisfy the general condition that > 21 = "Bust"
            total_values = [x for x in total_values if x < 22]
            print("Value: " + ("".join(str(total_values))))


if __name__ == "__main__":
    pass
