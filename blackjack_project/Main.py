"""
Main.py - Blackjack game main run file.
"""
import os
import Functions
import Objects

class BlackJackGame:
    """
    Main wrapper class containing game interface functionality.
    """

    def Welcome(self, Version: str):
        """
        Welcome message
        """
        print("""\nWelcome to BlackJack!\n
        (C) 2022 - Lawrence Short
        lawrence.short@BJSS.com
        Version: """ + str(Version) + "\n")
        BlackJackGame.SelectPlayers(self)


    """
    Game welcome interface functions:
    """
    def SelectPlayers(self):
        """
        Player selection interface
        """
        NumberOfPlayers = Functions.Logical.GetUserInputPostitiveInteger("Enter number of human players")
        if not NumberOfPlayers:
            print("Error - Please select number of players (remember: positive integer values only)")
            BlackJackGame.SelectPlayers(self)
        BlackJackGame.NamePlayers(self,NumberOfPlayers)

    def SelectDeck(self, Players: list):
        """
        Deck selection interface
        """
        NumberOfDecks = Functions.Logical.GetUserInputPostitiveInteger("Enter number of decks")
        if not NumberOfDecks:
            print("Error - Please select number of desks (remember: positive integer values only)")
            BlackJackGame.SelectDeck(self, Players)
        # insert update of player object
        print(str(NumberOfDecks) + " selected! (" + str(int(NumberOfDecks)*52) + " cards)")
        BlackJackGame.StartGame(self, Players, NumberOfDecks)

    def NamePlayers(self, NumberOfPlayers: int):
        """
        Player name interface
        """
        Players = []
        for i in range(0,NumberOfPlayers):
            PlayerName = BlackJackGame.GetPlayerName(self,i+1)
            Functions.Logical.NamePlayer(i+1,PlayerName)
            Player = Objects.Player(i+1,PlayerName)
            Players.append(Player)
        BlackJackGame.SelectDeck(self, Players)

    def GetPlayerName(self, PlayerID: int) -> str:
        """
        Get player name
        """
        PlayerName = Functions.Logical.GetUserInputString("Enter player " + str(PlayerID) + " name")
        if Functions.Logical.ValidateName(PlayerName):
            return str(PlayerName)
        print("Error - Incorrect name format (remember: must be > 1 character)")
        BlackJackGame.GetPlayerName(self, PlayerID)


    """
    Game operation interface
    """
    def StartGame(self, Players: list, NumberOfDecks: int):
        """
        game operation wrapper
        """
        os.system("clear")
        print("Game Starting..")
        # Creating the deck
        Deck = Functions.Logical.Randomise((Objects.Deck(NumberOfDecks).Deck))
        
        # initialise dealer
        Dealer = Objects.Player(0,"Dealer")
        round = 0

        while True:
            os.system("clear")
            round += 1
            print("HAND " + str(round))
            Scores = {}
            for Player in Players:
                Deck, Card1 = Objects.Deck.DrawCard(Deck)
                Deck, Card2 = Objects.Deck.DrawCard(Deck)
                Player.Hand = Objects.Hand(Card1,Card2)
                print(f"\nPlayer: {Player.Name} Hand:\n")

                for Card in Player.Hand.Hand:
                    Objects.Card.Describe(Card)
                Objects.Hand.PrintHandValue(Player.Hand.Hand)

                while True:
                    Option = Functions.Logical.GetStickOrTwistInput()

                    if Option == 'twist':
                        Deck, Card = Objects.Deck.DrawCard(Deck)
                        Objects.Card.Describe(Card)
                    else:
                        Scores[Player.Name] = Objects.Hand.HandValue(Player.Hand.Hand)
                        break    

                    Player.Hand.Hand = Objects.Hand.HandTwist(Player.Hand.Hand,Card)

                    Objects.Hand.PrintHandValue(Player.Hand.Hand)
                    if all(x > 21 for x in Objects.Hand.HandValue(Player.Hand.Hand)):
                        Scores[Player.Name] = -1
                        break

                Objects.Deck.PrintCardsInDeck(Deck)

            # dealer's turn
            print("\n Dealer's Turn.\n")
            # Dealer's hand:
            Deck, Card1 = Objects.Deck.DrawCard(Deck)
            Deck, Card2 = Objects.Deck.DrawCard(Deck)
            Dealer.Hand = Objects.Hand(Card1,Card2)
            #for Card in Dealer.Hand.Hand:
            #    Objects.Card.Describe(Card)
            #    pass

            # add dealer's score
            # add dealer's logic

            break

        # at end of round:

        Players = Functions.Logical.ShiftPlayerOrder(Players)






# need to build something in to have a maximum number of users

    def __init__(self):
        """_summary_

        Args:
            self (_type_): _description_
        """
        BlackJackGame.Welcome(self,"1.1")
# remember ace high or low




if __name__ == "__main__":
    BlackJackGame()
