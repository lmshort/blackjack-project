"""
Main.py - Blackjack game main run file.
"""
import os
import time
from blackjack_project import Functions
from blackjack_project import Objects
from typing import Union
"""
To DO:
- add tests for all (just missing Main - key game ones)
- check pylint
- reformat with black
"""

class BlackJackGame:
    """
    Main wrapper class containing game interface functionality.
    """

    def Welcome(self, Version: str):
        """_Summary_
        Display welcome message upon game start.
        
        Args:
            Version (str): Game version number.
        """
        print("""\nWelcome to BlackJack!\n
        (C) 2022 - Lawrence Short
        lawrence.short@BJSS.com
        Version: """ + str(Version) + "\n")

    def GameTime() -> int:
        """_Summary_
        Constant value game time, used throughout.

        Returns:
            float: No. seconds
        """
        return 2

    """
    Game welcome interface functions:
    """
    def SelectPlayers(self) -> int:
        """_summary_
        Select, via user input the number of players required (maximum 5).

        Returns:
            NumberOfPlayers (int): Number of players required (maximum 5).
        """
        NumberOfPlayers = Functions.Logical.GetUserInputPostitiveInteger("Enter number of human players")
        if not NumberOfPlayers:
            print("Error - Please select number of players (remember: positive integer values only)")
            BlackJackGame.SelectPlayers(self)
        else:
            return NumberOfPlayers

    def SelectDeck(self, Players: list) -> int:
        """_summary_
        Select the number of decks required for this game, (maximum 5).

        Args:
            Players (list): List of player objects.

        Returns:
            int: Number of game decks (maximum 5).
        """
        NumberOfDecks = Functions.Logical.GetUserInputPostitiveInteger("Enter number of decks")
        if not NumberOfDecks:
            print("Error - Please select number of desks (remember: positive integer values only)")
            BlackJackGame.SelectDeck(self, Players)
        # insert update of player object
        print(str(NumberOfDecks) + " selected! (" + str(int(NumberOfDecks)*52) + " cards)")
        return NumberOfDecks
        
    def NamePlayers(self, NumberOfPlayers: int) -> list:
        """_summary_
        Obtain and record individual player names.

        Args:
            NumberOfPlayers (int): Number of players required (maximum 5).

        Returns:
            Players (list): List of player objects required for the game (minus Dealer).
        """
        Players = []
        for i in range(0,NumberOfPlayers):
            PlayerName = Functions.Logical.GetPlayerName(i+1)
            Player = Objects.Player(i+1,PlayerName)
            Players.append(Player)
        return Players

    """
    Game operation interface functions
    """
    def StartGame(self, Players: list, NumberOfDecks: int):
        """_summary_
        Main game interface wrapper. This function contains executes gameplay indefinitely.

        Args:
            Players (list): List of player objects.
            NumberOfDecks (int): Number of decks required for the game (maximum 5).
        """
        os.system("clear")
        print("Game Starting..")

        # Deck generation
        Deck = Functions.Logical.Randomise((Objects.Deck(NumberOfDecks).Deck))
        
        # Round iterator and score dict initialised
        RoundNum = 0
        Scores = {}

        while True:
            # Executes interface for players' turns.
            Deck, RoundNum, Scores = BlackJackGame.PlayersTurn(self, Deck, RoundNum, Players, Scores)
            time.sleep(0.75 * BlackJackGame.GameTime())
            # Executes Dealer's turn
            Deck, Scores = BlackJackGame.DealersTurn(self, Deck, Scores)
            time.sleep(0.75 * BlackJackGame.GameTime())
            print("Deck has " + str(Objects.Deck.CountCardsInDeck(Deck)) + " cards left.")
            time.sleep(0.75 * BlackJackGame.GameTime())
            # Evaulaute the winners/losers
            Players = BlackJackGame.AssessResults(self, Players, Scores)
            time.sleep(1.5 * BlackJackGame.GameTime())
            os.system("clear")
            # Presentation of overall results
            BlackJackGame.OverallStandings(self, Players)
            time.sleep(1.5 * BlackJackGame.GameTime())
            # Hard reshuffle when less than 25 cards.
            if (Objects.Deck.CountCardsInDeck(Deck)) <= 25:
                print("Re-shuffling Deck...")
                time.sleep(0.8 * BlackJackGame.GameTime())
                Deck = Functions.Logical.Randomise((Objects.Deck(NumberOfDecks).Deck))
            # at end of Round - player order is shifted
            Players = Functions.Logical.ShiftPlayerOrder(Players)
            # Next hand countdown
            Functions.Numeric.CountInNewHand

    def PlayersTurn(self, Deck: object, RoundNum: int, Players: list, Scores: dict) -> Union[object, int, dict]:
        """_summary_
        Executes all players' turns.

        Args:
            Deck (object): Game deck of cards.
            RoundNum (int): Game round number, iterated each time this function is called.
            Players (list): List of player objects (maximum 5).
            Scores (dict): Dictionary containing scores for the round.

        Returns:
            Deck (object): Game deck of cards - with X cards removed for player draws.
            RoundNum (int): Game round number.
            Players (list): List of player objects (maximum 5).
            Scores (dict): Dictionary containing scores for the round.
        """
        os.system("clear")
        RoundNum += 1
        print("HAND " + str(RoundNum))
        for Player in Players:
            Deck, Player = BlackJackGame.BuildHand(self, Deck, Player)
            print(f"\nPlayer: {Player.Name}'s Hand:\n")

            for Card in Player.Hand.Hand:
                Objects.Card.Describe(Card)
            Objects.Hand.PrintHandValue(Player.Hand.Hand)

            # Execution of function to interface user stick/twist options
            Deck, Scores = BlackJackGame.UserOptions(self, Deck, Player, Scores)

        return Deck, RoundNum, Scores

    def BuildHand(self, Deck: object, Player: object) -> Union[object,object]:
        """_summary_
        Constructs a player/dealer's hand by drawing 2 cards from the deck.

        Args:
            Deck (object): Deck of playing cards
            Player (object): player or dealer 

        Returns:
            Deck (object): Deck of playing cards
            Player (oject): Player object (containing hand attribute list of cards)
        """
        Deck, Card1 = Objects.Deck.DrawCard(Deck)
        Deck, Card2 = Objects.Deck.DrawCard(Deck)
        Player.Hand = Objects.Hand(Card1,Card2)
        return Deck, Player

    def UserOptions(self, Deck: object, Player: object, Scores: dict) -> Union[object, dict]:
        """_summary_
        Loops through iterations of user options to either stick or twist.

        Args:
            Deck (object): Deck of playing cards
            Player (object): Single player object
            Scores (dict): Game scores dictionary

        Returns:
            Deck (object): Deck of playing cards
            Scores (dict): Game scores dictionary 
        """
        # migrate this all over to a separate function
        while True:
            # get user option
            Option = Functions.Logical.GetStickOrTwistInput()
            time.sleep(0.4 * BlackJackGame.GameTime())
            if Option == 'twist':
                # draw card
                Deck, Card = Objects.Deck.DrawCard(Deck)
                Objects.Card.Describe(Card)
            else:
                # stick option sets score and exists function
                Scores[Player.Name] = Objects.Hand.HandValue(Player.Hand.Hand)
                break    

            # append card to player's hand
            Player.Hand.Hand = Objects.Hand.HandTwist(Player.Hand.Hand,Card)
            Objects.Hand.PrintHandValue(Player.Hand.Hand)

            # evaluate whether player's hand is "bust" and adjusting score if so.
            if all(x > 21 for x in Objects.Hand.HandValue(Player.Hand.Hand)):
                Scores[Player.Name] = [-1]
                break    
        return Deck, Scores

    def DealersTurn(self, Deck: object, Scores: dict) -> Union[object, dict]:
        """_summary_
        Executes dealer's turn.

        Args:
            Deck (object): Game deck of cards.
            Scores (dict): Dictionary containing scores for the round.

        Returns:
            Deck (object): Game deck of cards - with X cards removed for player draws.
            Scores (dict): Dictionary containing scores for the round.
        """
        print("\n Dealer's Turn.\n")
        Dealer = Objects.Player(0,"Dealer")

        # Dealer's hand:
        Deck, Dealer = BlackJackGame.BuildHand(self, Deck, Dealer)
        print(f"\nDealer's Hand:\n")
        for Card in Dealer.Hand.Hand:
            Objects.Card.Describe(Card)
        Objects.Hand.PrintHandValue(Dealer.Hand.Hand)

        time.sleep(0.4 * BlackJackGame.GameTime())

        # Executes logic behind dealer's turn
        Deck, Scores = BlackJackGame.DealerOptions(self, Dealer, Deck, Scores)
        return Deck, Scores  

    def DealerOptions(self, Dealer: object, Deck: object, Scores: dict) -> Union[object, dict]:
        """_summary_
        Undertakes dealer options (automated process).

        Args:
            Dealer (object): Dealer "player" object
            Deck (object): Deck of playing cards
            Scores (dict): Game scores dictionary

        Returns:
            Deck (object): Deck of playing cards
            Scores (dict): Games scores dictionary
        """
        # runs until exit conditions are met
        while True:
            DealerHandValueMax = max(Objects.Hand.HandValue(Dealer.Hand.Hand))
            DealerHandValueMin = min(Objects.Hand.HandValue(Dealer.Hand.Hand))
            # if the hand value is within 16-22, then register score and exist operation
            if DealerHandValueMax <= 21 and DealerHandValueMax > 16:
                Scores["Dealer"] = Objects.Hand.HandValue(Dealer.Hand.Hand)
                break
            elif DealerHandValueMin <= 21 and DealerHandValueMin > 16:
                Scores["Dealer"] = Objects.Hand.HandValue(Dealer.Hand.Hand)
                break

            # if the above conditions are not met, dealer will always draw a card
            Deck, Card = Objects.Deck.DrawCard(Deck)
            Objects.Card.Describe(Card)
            time.sleep(0.4 * BlackJackGame.GameTime())

            # hand adjusted
            Dealer.Hand.Hand = Objects.Hand.HandTwist(Dealer.Hand.Hand,Card)
            Objects.Hand.PrintHandValue(Dealer.Hand.Hand)

            # condition checks if dealer is "bust"
            if all(x > 21 for x in Objects.Hand.HandValue(Dealer.Hand.Hand)):
                Scores["Dealer"] = [-1]
                break   
        return Deck, Scores  

    def AssessResults(self, Players: list, Scores: dict) -> list:
        """_summary_
        Assesses wins/ties/losses and allocates them to the corresponding player.

        Args:
            Players (list): List of player objects (maximum 5).
            Scores (dict): Scores (dict): Dictionary containing scores for the round.

        Returns:
            Players (list): List of player objects (maximum 5).
        """
        # Obtain index reference for a given player.
        PlayerReference = {}
        for index, Player in enumerate(Players):
            PlayerReference[Player.Name] = index

        # Runs through scores and evaluates status.
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

    def OverallStandings(self, Players: list):
        """_summary_
        Presentation of the overall player standings.

        Args:
            Players (list): List of player objects (maximum 5).
        """
        print("\nOVERALL STANDINGS")
        for Player in Players:
            print(f"\nPlayer: {Player.Name}")
            print("Total Wins: " + str(Player.Wins))
            print("Total Ties: " + str(Player.Ties))
            print("Total Losses: " + str(Player.Losses))
    

    def __init__(self):
        """_summary_
        Initiator functionality. Executes through introductory functions before starting the game.

        Args:
            self (_type_): _description_
        """
        BlackJackGame.Welcome(self,"1.1")
        NumberOfPlayers = BlackJackGame.SelectPlayers(self)
        Players = BlackJackGame.NamePlayers(self,NumberOfPlayers)
        NumberOfDecks = BlackJackGame.SelectDeck(self, Players)
        BlackJackGame.StartGame(self, Players, NumberOfDecks)

# remember ace high or low


if __name__ == "__main__":
    BlackJackGame()
