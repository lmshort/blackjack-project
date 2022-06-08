"""
Main.py - Blackjack game main run file.
"""
import os
import time
from typing import Union
from blackjack_project import functions
from blackjack_project import objects

GAME_TIME = 2


class BlackjackGame:
    """
    Main wrapper class containing game interface functionality.
    """

    def welcome(version: str):
        """Display welcome message upon game start.

        Args:
            version (str): Game version number.
        """
        print(
            """\nWelcome to BlackJack!\n
        (C) 2022 - Lawrence Short
        lawrence.short@BJSS.com
        Version: """
            + str(version)
            + "\n"
        )

    def select_players(self) -> int:
        """Select, via user input the number of players required (maximum 5).

        Returns:
            number_of_players (int): Number of players required (maximum 5).
        """
        while True:
            number_of_players = functions.Logical.get_user_input_positive_integer(
                "Enter number of human players"
            )
            if not number_of_players:
                print(
                    "Error - Please select number of players (remember: positive integer values only)"
                )
            else:
                return number_of_players

    def select_deck(self, players: list) -> int:
        """Select the number of decks required for this game, (maximum 5).

        Args:
            players (list): List of player objects.

        Returns:
            int: Number of game decks (maximum 5).
        """
        number_of_decks = functions.Logical.get_user_input_positive_integer(
            "Enter number of decks"
        )
        if not number_of_decks:
            print(
                "Error - Please select number of desks (remember: positive integer values only)"
            )
            BlackjackGame.select_deck(self, players)
        # insert update of player object
        print(
            str(number_of_decks)
            + " selected! ("
            + str(int(number_of_decks) * 52)
            + " cards)"
        )
        return number_of_decks

    def name_players(number_of_players: int) -> list:
        """Obtain and record individual player names.

        Args:
            number_of_players (int): Number of players required (maximum 5).

        Returns:
            players (list): List of player objects required for the game (minus Dealer).
        """
        players = []
        for i in range(0, number_of_players):
            player_name = functions.Logical.get_player_name(i + 1)
            player = objects.Player(i + 1, player_name)
            players.append(player)
        return players

    def start_game(self, players: list, number_of_decks: int):
        """Main game interface wrapper. This function contains executes gameplay indefinitely.

        Args:
            players (list): List of player objects.
            number_of_decks (int): Number of decks required for the game (maximum 5).
        """
        os.system("clear")
        print("Game Starting..")

        # Deck generation
        deck = functions.Logical.randomise((objects.Deck(number_of_decks).deck))
        print(len(deck))
        # Round iterator and score dict initialised
        round_num = 0
        scores = {}

        while True:
            # Executes interface for players' turns.
            deck, round_num, scores = BlackjackGame.players_turn(
                self, deck, round_num, players, scores
            )
            time.sleep(0.75 * GAME_TIME)
            # Executes Dealer's turn
            deck, scores = BlackjackGame.dealers_turn(self, deck, scores)
            time.sleep(0.75 * GAME_TIME)
            print(
                "Deck has "
                + str(objects.Deck.count_cards_in_deck(deck))
                + " cards left."
            )
            time.sleep(0.75 * GAME_TIME)
            # Evaulaute the winners/losers
            players = BlackjackGame.assess_results(players, scores)
            time.sleep(1.5 * GAME_TIME)
            os.system("clear")
            # Presentation of overall results
            BlackjackGame.overall_standings(players)
            time.sleep(1.5 * GAME_TIME)
            # Hard reshuffle when less than 25 cards.
            if (objects.Deck.count_cards_in_deck(deck)) <= 25:
                print("Re-shuffling Deck...")
                time.sleep(0.8 * GAME_TIME)
                deck = functions.Logical.randomise((objects.Deck(number_of_decks).deck))
            # at end of Round - player order is shifted
            players = functions.Logical.shift_player_order(players)
            # Next hand countdown
            functions.Numeric.count_in_new_hand

    def players_turn(
        self, deck: object, round_num: int, players: list, scores: dict
    ) -> Union[object, int, dict]:
        """Executes all players' turns.

        Args:
            dseck (object): Game deck of cards.
            round_num (int): Game round number, iterated each time this function is called.
            players (list): List of player objects (maximum 5).
            scores (dict): Dictionary containing scores for the round.

        Returns:
            deck (object): Game deck of cards - with X cards removed for player draws.
            round_num (int): Game round number.
            players (list): List of player objects (maximum 5).
            scores (dict): Dictionary containing scores for the round.
        """
        os.system("clear")
        round_num += 1
        print("HAND " + str(round_num))
        for player in players:

            print(f"\nPlayer: {player.name}'s Hand:\n")
            deck, player = BlackjackGame.build_hand(self, deck, player)
            for card in player.hand:
                objects.Card.describe(card)
            objects.Hand.print_hand_value(player.hand)

            # Execution of function to interface user stick/twist options
            deck, scores = BlackjackGame.user_options(deck, player, scores)

        return deck, round_num, scores

    def build_hand(self, deck: object, player: object) -> Union[object, object]:
        """Constructs a player/dealer's hand by drawing 2 cards from the deck.

        Args:
            deck (object): Deck of playing cards
            player (object): player or dealer

        Returns:
            deck (object): Deck of playing cards
            player (oject): Player object (containing hand attribute list of cards)
        """
        deck, card1 = objects.Deck.draw_card(deck)
        deck, card2 = objects.Deck.draw_card(deck)
        player.hand = objects.Hand.deal_hand(self, card1, card2)
        return deck, player

    def user_options(deck: list, player: object, scores: dict) -> Union[object, dict]:
        """_summary_
        Loops through iterations of user options to either stick or twist.

        Args:
            deck (object): Deck of playing cards
            player (object): Single player object
            scores (dict): Game scores dictionary

        Returns:
            deckreurned (object): Deck of playing cards
            scores (dict): Game scores dictionary
        """
        # migrate this all over to a separate function
        while True:
            # get user option
            option = functions.Logical.get_stick_or_twist_input()
            time.sleep(0.4 * GAME_TIME)
            if option == "twist":
                # draw card
                deck, card = objects.Deck.draw_card(deck)
                objects.Card.describe(card)
            else:
                # stick option sets score and exists function
                scores[player.name] = objects.Hand.hand_value(player.hand)
                break

            # append card to player's hand
            player.hand = objects.Hand.hand_twist(player.hand, card)
            objects.Hand.print_hand_value(player.hand)

            # evaluate whether player's hand is "bust" and adjusting score if so.
            if all(x > 21 for x in objects.Hand.hand_value(player.hand)):
                scores[player.name] = [-1]
                break
        return deck, scores

    def dealers_turn(self, deck: object, scores: dict) -> Union[object, dict]:
        """Executes dealer's turn.

        Args:
            deck (object): Game deck of cards.
            scores (dict): Dictionary containing scores for the round.

        Returns:
            deck (object): Game deck of cards - with X cards removed for player draws.
            scores (dict): Dictionary containing scores for the round.
        """
        print("\n Dealer's Turn.\n")
        dealer = objects.Player(0, "Dealer")

        # Dealer's hand:
        deck, dealer = BlackjackGame.build_hand(self, deck, dealer)
        print("\nDealer's Hand:\n")
        for card in dealer.hand:
            objects.Card.describe(card)
        objects.Hand.print_hand_value(dealer.hand)

        time.sleep(0.4 * GAME_TIME)

        # Executes logic behind dealer's turn
        deck, scores = BlackjackGame.dealer_options(self, dealer, deck, scores)
        return deck, scores

    def dealer_options(
        self, dealer: object, deck: object, scores: dict
    ) -> Union[object, dict]:
        """Undertakes dealer options (automated process).

        Args:
            dealer (object): Dealer "player" object
            deck (object): Deck of playing cards
            scores (dict): Game scores dictionary

        Returns:
            deck (object): Deck of playing cards
            scores (dict): Games scores dictionary
        """
        # runs until exit conditions are met
        while True:
            dealer_hand_max_value = max(objects.Hand.hand_value(dealer.hand))
            dealer_hand_min_value = min(objects.Hand.hand_value(dealer.hand))
            # if the hand value is within 16-22, then register score and exist operation
            if 16 < dealer_hand_max_value <= 21:
                scores["Dealer"] = objects.Hand.hand_value(dealer.hand)
                break
            elif 16 < dealer_hand_min_value <= 21:
                scores["Dealer"] = objects.Hand.hand_value(dealer.hand)
                break

            # if the above conditions are not met, dealer will always draw a card
            deck, card = objects.Deck.draw_card(deck)
            objects.Card.describe(card)
            time.sleep(0.4 * GAME_TIME)

            # hand adjusted
            dealer.hand = objects.Hand.hand_twist(dealer.hand, card)
            objects.Hand.print_hand_value(dealer.hand)

            # condition checks if dealer is "bust"
            if all(x > 21 for x in objects.Hand.hand_value(dealer.hand)):
                scores["Dealer"] = [-1]
                break
        return deck, scores

    def assess_results(players: list, scores: dict) -> list:
        """Assesses wins/ties/losses and allocates them to the corresponding player.

        Args:
            players (list): List of player objects (maximum 5).
            scores (dict): Scores (dict): Dictionary containing scores for the round.

        Returns:
            players (list): List of player objects (maximum 5).
        """
        # Obtain index reference for a given player.
        player_reference = {}
        for index, player in enumerate(players):
            player_reference[player.name] = index

        # Runs through scores and evaluates status.
        keys = list(scores.keys())
        for key in keys:
            if key != "Dealer":
                if max(scores[key]) > max(scores["Dealer"]):
                    print("Player: " + key + " wins!")
                    players[player_reference[key]].wins += 1
                elif max(scores[key]) == max(scores["Dealer"]):
                    print("Player: " + key + " ties.")
                    players[player_reference[key]].ties += 1
                else:
                    print("Player: " + key + " loses.")
                    players[player_reference[key]].losses += 1
        return players

    def overall_standings(players: list):
        """Presentation of the overall player standings.

        Args:
            players (list): List of player objects (maximum 5).
        """
        print("\nOVERALL STANDINGS")
        for player in players:
            print(f"\nPlayer: {player.name}")
            print("Total Wins: " + str(player.wins))
            print("Total Ties: " + str(player.ties))
            print("Total Losses: " + str(player.losses))

    def __init__(self):
        """Initiator functionality. Executes through introductory functions before starting the game.

        Args:
            self (_type_): _description
        """
        BlackjackGame.welcome("1.1")
        number_of_players = BlackjackGame.select_players(self)
        players = BlackjackGame.name_players(number_of_players)
        number_of_decks = BlackjackGame.select_deck(self, players)
        BlackjackGame.start_game(self, players, number_of_decks)


# remember ace high or low


if __name__ == "__main__":
    BlackjackGame()
