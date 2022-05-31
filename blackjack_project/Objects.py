from typing import Union

class Player:
    """
    Player class - created for each player added to the game, contains overall information and stats.
    """
    def __init__ (Self, PlayerID: int, PlayerName: str):
        """_summary_
        Player class initiated with overall information and stats.

        Args:
            Self (object): Player object
            PlayerID (int): Simple integer used to account for differences when PlayerName is duplicately used.
            PlayerName (str): Player name string
        """
        Self.ID = PlayerID
        Self.Name = PlayerName
        #Self.Money = 100
        Self.Wins = 0
        Self.Losses = 0
        Self.Ties = 0
        Self.Hand = None


class Deck:
    """
    Deck class - a class container where list of Card objects are stored.
    """
    def __init__ (Self, NumberOfDecks: int):
        """_summary_
        Deck class initiated with no. decks and deck attribute, a list of cards.

        Args:
            Self (object): Deck object
            NumberOfDecks (int): Number of decks to be used
        """
        Self.NumberOfDecks = NumberOfDecks
        Self.Deck = Deck.GenerateDeck(NumberOfDecks)
        # include cards and suits

    def GenerateDeck(NumberOfDecks: int) -> list:
        """_summary_
        Generate the deck from card objects, based on specified number of decks.

        Args:
            NumberOfDecks (int): Number of decks to be used

        Returns:
            list: list of card objects representing a deck
        """
        Deck = []
        for _ in range(0, NumberOfDecks):
            for j in range(1, 14):
                for k in ('Diamond','Heart','Spade','Club'):
                    Deck.append(Card(j,k))
        return Deck

    def DrawCard(Self) -> Union[object, object]:
        """_summary_
        Draws a card from a deck.

        Args:
            Self (list): Deck Deck attribute (represents a list of cards)

        Returns:
            object: Deck Deck attribute (list of cards)
            object: Card object, representing the drawn card/
        """
        DrawnCard = Self.pop(0)
        Self.pop(0)
        return Self, DrawnCard
                    
    def CountCardsInDeck(Self) -> int:
        """_summary_
        Count the number of cards in a deck

        Args:
            Self (list): Deck Deck attribute (represents a list of cards)

        Returns:
            int: number of cards left in the deck
        """
        return len(Self)


class Card:
    """
    Card class - card represents a single game card, with real-life attributes assigned.
    """
    def __init__(Self, CardNumber: int, CardSuit: str):
        """_summary_
        Initiator function defines key attributes for a card.

        Args:
            Self (object): card object
            CardNumber (int): card number - ranges from 1-13
            CardSuit (str): string suit classification (4 options)
        """
        Self.Number = CardNumber
        Self.Picture = Card.AssignPicture(CardNumber)
        Self.Suit = CardSuit
        Self.SuitRank = Card.AssignRank(CardSuit)
        Self.Value = Card.CardValue(CardNumber)

    def AssignPicture(CardNumber: int) -> str:
        """_summary_
        Assigns a picture attribute, based on card number.

        Args:
            CardNumber (int): card number assigned.

        Returns:
            str: textual description of the card, should it be a "picture" card
        """
        PictureOptions = {1: 'Ace', 11 : 'Jack', 12 : 'Queen', 13 : 'King'}
        if CardNumber in PictureOptions:
            return PictureOptions[CardNumber]

    def AssignRank(Suit: str) -> int:
        """_summary_
        Assigns a rank, based on its given suit.

        Args:
            Suit (str): given card suit

        Returns:
            int: ranking, based on suit (1 -> 4)
        """
        RankOptions = {'Diamond' : 1, 'Heart' : 2, 'Spade' : 3, 'Club' : 4}
        if Suit in RankOptions:
            return RankOptions[Suit]       

    def Describe(Self):
        """_summary_
        Prints a description of a given card.

        Args:
            Self (object): card object
        """
        if Self.Number not in (1,11,12,13):
            print(f"{Self.Number} of {Self.Suit}s")
        elif Self.Number in (1,11,12,13):
            print(f"{Self.Picture} of {Self.Suit}s")

    def CardValue(CardNumber: int) -> int:
        """_summary_
        Returns the card value 

        Args:
            Self (object): card object
            CardNumber (int): _description_

        Returns:
            int: _description_
        """
        if CardNumber > 10:
            CardValue = 10
        else:
            CardValue = CardNumber
        return CardValue



class Hand():
    """
    Hand class represents a player's collection of cards.
    """
    def __init__(Self, Card1: object, Card2: object):
        """_summary_
        Initiator function defines the hand attribute "Hand" - a list of cards, based on initial 2 card draw.

        Args:
            Self (object): Hand object
            Card1 (object): Drawn card 1
            Card2 (object): Drawn card 2
        """
        Self.Hand = Hand.DealHand(Self,Card1, Card2)

    def DealHand(Self, Card1: object, Card2: object) -> list:
        """_summary_
        Function deals a hand, creating a list of card objects for an initial deal.

        Args:
            Self (object): Hand object
            Card1 (object): Drawn card 1
            Card2 (object): Drawn card 2

        Returns:
            object: Hand Hand attribute, a list of cards.
        """
        Self.Hand = [Card1,Card2]
        return Self.Hand

    def HandTwist(Self, Card: object) -> list:
        """_summary_
        Draws a single card.

        Args:
            Self (list): Hand Hand attribute - list of cards
            Card (object): Drawn card

        Returns:
            list: Hand Hand attribute - list of cards
        """
        Self.append(Card)
        return Self

    def HandValue(Self) -> list:
        """_summary_
        Determines potential hand values, based on cards in hand.

        Args:
            Self (list): Hand Hand attribute - list of cards

        Returns:
            list: List of possible values, based on card combinations
        """
        # Initiate array with a 0 value.
        TotalValues = [0]
        for Card in Self:
            # If not an "ace" card, value is added to each array element.
            if Card.Value != 1:
                TotalValues = [x+Card.Value for x in TotalValues]
            # If an "ace" card, additional combinations possible, each accounted for.
            else:
                TotalValuesPrevious = TotalValues
                TotalValues = [x+1 for x in TotalValues]
                for value in TotalValuesPrevious:
                    TotalValues.append(value + 11)
        return TotalValues

    def PrintHandValue(Self):
        """_summary_
        Prints the hand card value.

        Args:
            Self (list): Hand Hand attribute - a list of cards
        """
        TotalValues = Hand.HandValue(Self)
        if all(Value > 21 for Value in TotalValues):
            print("BUST!")
        else:
            # Just returns the values which satisfy the general condition that > 21 = "Bust"
            TotalValues = [x for x in TotalValues if x < 22]
            print("Value: " + (''.join(str(TotalValues))))


if __name__ == "__main__":
    pass
