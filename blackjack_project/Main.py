"""
Main.py - Blackjack game main run file.
"""
import os
import Functions
import Objects
import time

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
    Game operation interface functions
    """
    def StartGame(self, Players: list, NumberOfDecks: int):
        """
        game operation wrapper
        """
        os.system("clear")
        print("Game Starting..")

        # Creating the deck
        Deck = Functions.Logical.Randomise((Objects.Deck(NumberOfDecks).Deck))
        
        RoundNum = 0
        # Creating dictionary for scores to be contained
        Scores = {}

        while True:
            Deck, RoundNum, Players, Scores = BlackJackGame.PlayersTurn(self, Deck, RoundNum, Players, Scores)
            time.sleep(0.4)
            Deck, Scores = BlackJackGame.DealersTurn(self, Deck, Scores)
            time.sleep(0.4)
            Objects.Deck.PrintCardsInDeck(Deck)
            time.sleep(0.4)
            Players = BlackJackGame.AssessResults(self, Players, Scores)
            time.sleep(1.5)
            os.system("clear")
            BlackJackGame.OverallStandings(self, Players, RoundNum)
            time.sleep(0.4)
            if (Functions.Numeric.CountInNewHand) <= 25:
                print("Re-shuffling Deck...")
                time.sleep(0.4)
                Deck = Functions.Logical.Randomise((Objects.Deck(NumberOfDecks).Deck))
            # at end of Round:
            Players = Functions.Logical.ShiftPlayerOrder(Players)


# functions to be cleaned and adjusted:
    def PlayersTurn(self, Deck: object, RoundNum: int, Players: list, Scores: dict):
        """_summary_

        Args:
            Deck (object): _description_
            RoundNum (int): _description_
            Players (list): _description_
            Scores (dict): _description_

        Returns:
            _type_: _description_
        """
        os.system("clear")
        RoundNum += 1
        print("HAND " + str(RoundNum))
        for Player in Players:
            Deck, Card1 = Objects.Deck.DrawCard(Deck)
            Deck, Card2 = Objects.Deck.DrawCard(Deck)
            Player.Hand = Objects.Hand(Card1,Card2)
            print(f"\nPlayer: {Player.Name}'s Hand:\n")

            for Card in Player.Hand.Hand:
                Objects.Card.Describe(Card)
            Objects.Hand.PrintHandValue(Player.Hand.Hand)

            # migrate this all over to a separate function
            while True:
                Option = Functions.Logical.GetStickOrTwistInput()
                time.sleep(0.4)
                if Option == 'twist':
                    Deck, Card = Objects.Deck.DrawCard(Deck)
                    Objects.Card.Describe(Card)
                else:
                    Scores[Player.Name] = Objects.Hand.HandValue(Player.Hand.Hand)
                    break    

                Player.Hand.Hand = Objects.Hand.HandTwist(Player.Hand.Hand,Card)

                Objects.Hand.PrintHandValue(Player.Hand.Hand)
                if all(x > 21 for x in Objects.Hand.HandValue(Player.Hand.Hand)):
                    Scores[Player.Name] = [-1]
                    break    
        return Deck, RoundNum, Players, Scores

    def DealersTurn(self, Deck: object, Scores: dict):
        """
        TBC
        """
        print("\n Dealer's Turn.\n")
        Dealer = Objects.Player(0,"Dealer")
        # Dealer's hand:
        Deck, Card1 = Objects.Deck.DrawCard(Deck)
        Deck, Card2 = Objects.Deck.DrawCard(Deck)
        Dealer.Hand = Objects.Hand(Card1,Card2)
        print(f"\nDealer's Hand:\n")
        for Card in Dealer.Hand.Hand:
            Objects.Card.Describe(Card)

        time.sleep(0.4)

        while True:
            DealerHandValueMax = max(Objects.Hand.HandValue(Dealer.Hand.Hand))
            DealerHandValueMin = min(Objects.Hand.HandValue(Dealer.Hand.Hand))
            if DealerHandValueMax <= 21 and DealerHandValueMax > 16:
                Scores["Dealer"] = Objects.Hand.HandValue(Dealer.Hand.Hand)
                break
            elif DealerHandValueMin <= 21 and DealerHandValueMin > 16:
                Scores["Dealer"] = Objects.Hand.HandValue(Dealer.Hand.Hand)
                break
            Deck, Card = Objects.Deck.DrawCard(Deck)
            Objects.Card.Describe(Card)
            time.sleep(0.4)
            Dealer.Hand.Hand = Objects.Hand.HandTwist(Dealer.Hand.Hand,Card)
            Objects.Hand.PrintHandValue(Dealer.Hand.Hand)
            if all(x > 21 for x in Objects.Hand.HandValue(Dealer.Hand.Hand)):
                Scores["Dealer"] = [-1]
                break   
        return Deck, Scores  


    def AssessResults(self, Players: list, Scores: dict):
        """_summary_

        Args:
            Players (list): _description_
            Scores (dict): _description_

        Returns:
            _type_: _description_
        """
        PlayerReference = {}
        for index, Player in enumerate(Players):
            PlayerReference[Player.Name] = index

        keys = list(Scores.keys())
        for key in keys:
            if key != "Dealer":
                if max(Scores[key]) > max(Scores["Dealer"]):
                    print("Player: " + key + " wins!")
                    Players[PlayerReference[key]].Wins += 1
                elif max(Scores[key]) == max(Scores["Dealer"]):
                    print("Player: " + key + " ties.")
                    Players[PlayerReference[key]].Ties += 1
                else:
                    print("Player: " + key + " loses.")
                    Players[PlayerReference[key]].Losses += 1
        return Players

    def OverallStandings(self, Players: list, RoundNum: int):
        """_summary_

        Args:
            Players (_type_): _description_
        """
        print("\nOVERALL STANDINGS")
        for Player in Players:
            print(f"\nPlayer: {Player.Name}")
            print("Total Wins: " + str(Player.Wins))
            print("\nTotal Ties: " + str(Player.Ties))
            print("\nTotal Losses: " + str(Player.Losses))
    

# need to add a re-build deck when deck size < 30
# need to build something in to have a maximum number of users (5 max)
# need to build something in to have a maximum number of decks (10 max!!)


    def __init__(self):
        """_summary_

        Args:
            self (_type_): _description_
        """
        BlackJackGame.Welcome(self,"1.1")
# remember ace high or low




if __name__ == "__main__":
    BlackJackGame()
