
class Player:
    """
    Docstring TBC
    """
    def __init__ (Self, PlayerID: int, PlayerName: str):
        Self.ID = PlayerID
        Self.Name = PlayerName
        Self.Money = 100
        Self.Wins = 0
        Self.Losses = 0

    def PlayerWin(Self, Spoils: int):
        print("Player {Self.Name} wins " + str(Spoils) + ".")
        Self.Wins += 1
        Self.Money += Spoils

    def PlayerLoss(Self):
        print("Player {Self.Name} loses.")
        Self.Losses += 1
        Self.Money += -5

    def Describe(Self):
        print(Self)


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
                    

class Card:
    """
    Docstring TBC
    """
    def __init__(Self, CardNumber: int, CardSuit: str):
        Self.Number = CardNumber
        Self.Picture = Card.AssignPicture(Self,CardNumber)
        Self.Suit = CardSuit
        Self.SuitRank = Card.AssignRank(Self,CardSuit)

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


class Hand():
    pass


if __name__ == "__main__":
    pass


