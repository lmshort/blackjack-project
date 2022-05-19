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
        #for Card in Deck:
        #    Objects.Card.Describe(Card)

        exit
        
        # initialise dealer's hand

        #while True:
        
        for Player in Players:
            if Player.Name != "Dealer":
                print("\n" + str(Player.Name) + "'s Turn - Money~$" + str(Player.Money) + "\n")

                # receive cards

        
        # dealer's turn
        print("\n" + str(Player.Name) + "Dealer's Turn.\n")
        # at end of round:

        PlayerOrder = Functions.Logical.ShiftPlayerOrder(PlayerOrder)


    def Hand(self):
        """
        Docstring TBC
        """
        pass


    def __init__(self):
        """_summary_

        Args:
            self (_type_): _description_
        """
        BlackJackGame.Welcome(self,"1.1")
# remember ace high or low




if __name__ == "__main__":
    BlackJackGame()
