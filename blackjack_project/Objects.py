
class Player:
    """
    Docstring TBC
    """
    def __init__ (Self, PlayerID: int, PlayerName: str):
        Self.ID = PlayerID
        Self.Name = PlayerName
        #Self.Money = 100
        Self.Wins = 0
        Self.Losses = 0
        Self.Ties = 0
        Self.Hand = None

    def PlayerWin(Self, Spoils: int):
        print("Player {Self.Name} wins.")
        Self.Wins += 1
        #Self.Money += Spoils

    """
    def PlayerLoss(Self):
        print("Player {Self.Name} loses.")
        Self.Losses += 1
        Self.Money += -5
    """


class Deck:
    """
    Docstring TBC
    """
    def __init__ (Self, NumberOfDecks: int):
        Self.NumberOfDecks = NumberOfDecks
        Self.Deck = Deck.GenerateDeck(NumberOfDecks)
        # include cards and suits

    def GenerateDeck(NumberOfDecks: int):
        Deck = []
        for i in range(0, NumberOfDecks):
            for j in range(1, 14):
                for k in ('Diamond','Heart','Spade','Club'):
                    Deck.append(Card(j,k))
        return Deck

    def DrawCard(Self):
        """
        TBC
        """
        DrawnCard = Self.pop(0)
        Self.pop(0)
        return Self, DrawnCard
                    
    def CountCardsInDeck(Self):
        """
        TBC
        """
        return len(Self)


class Card:
    """
    Docstring TBC
    """
    def __init__(Self, CardNumber: int, CardSuit: str):
        Self.Number = CardNumber
        Self.Picture = Card.AssignPicture(Self,CardNumber)
        Self.Suit = CardSuit
        Self.SuitRank = Card.AssignRank(Self,CardSuit)
        Self.Value = Card.CardValue(Self,CardNumber)

    def AssignPicture(Self,CardNumber: int):
        PictureOptions = {1: 'Ace', 11 : 'Jack', 12 : 'Queen', 13 : 'King'}
        if CardNumber in PictureOptions:
            return PictureOptions[CardNumber]

    def AssignRank(Self, Suit: str):
        RankOptions = {'Diamond' : 1, 'Heart' : 2, 'Spade' : 3, 'Club' : 4}
        if Suit in RankOptions:
            return RankOptions[Suit]       

    def Describe(Self):
        if Self.Number not in (1,11,12,13):
            print(f"{Self.Number} of {Self.Suit}s")
        elif Self.Number in (1,11,12,13):
            print(f"{Self.Picture} of {Self.Suit}s")

    def CardValue(Self,CardNumber: int):
        if CardNumber > 10:
            CardValue = 10
        else:
            CardValue = CardNumber
        return CardValue



class Hand():
    def __init__(Self, Card1: object, Card2: object):
        Self.Hand = Hand.DealHand(Self,Card1, Card2)

    def DealHand(Self, Card1: object, Card2: object):
        Self.Hand = [Card1,Card2]
        return Self.Hand

    def HandTwist(Self, Card: object):
        Self.append(Card)
        return Self

    def HandValue(Self):
        TotalValues = [0]
        for Card in Self:
            if Card.Value != 1:
                TotalValues = [x+Card.Value for x in TotalValues]
            else:
                TotalValuesPrevious = TotalValues
                TotalValues = [x+1 for x in TotalValues]
                for value in TotalValuesPrevious:
                    TotalValues.append(value + 11)
        TotalValues = [x for x in TotalValues if x < 22]
        return TotalValues

    def PrintHandValue(Self):
        TotalValues = Hand.HandValue(Self)
        if all(Value > 21 for Value in TotalValues):
            print("BUST!")
        else: 
            print("Value: " + (''.join(str(TotalValues))))


if __name__ == "__main__":
    pass


