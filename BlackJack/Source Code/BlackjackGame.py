# Author: Sohaib Hussain
# Date: August 6, 2024
# Description: This class manages the game of Blackjack. It handles game initialization,
# player and dealer actions, betting, and game outcomes. It logs important events
# such as game start, player actions, and game results.

from Deck import Deck
from Player import Player
from Dealer import Dealer
from GLogger import GameLogger


class BlackjackGame:
    def __init__(self):
        """
        Initializes a new game of Blackjack with a player, dealer, and deck of cards.
        Sets the initial bet to 0 and starts the game. Logs the game start event.
        """
        self.logger = GameLogger()
        self.player = Player(credits=50)
        self.dealer = Dealer()
        self.deck = Deck()
        self.bet = 0
        self.player_turn_complete = False
        self.start_game()
        self.logger.log('Game started with player credits: 50')

    def start_game(self):
        """
        Initializes hands for the player and dealer, and starts a new game.

        Args:
            None

        Returns:
            None
        """
        self.player.hand = [self.deck.draw_card(), self.deck.draw_card()]
        self.dealer.hand = [self.deck.draw_card(), None]  # Dealer’s second card is hidden
        self.player_turn_complete = False
        self.logger.log(f'New game started. Player hand: {self.player.hand}')
        self.logger.log(f'Dealer hand: {self.dealer.hand}')

    def player_turn(self, action):
        """
        Handles the player's turn based on the action (hit or hold).

        Args:
            action (str): The player's action, either 'hit' or 'hold'.

        Returns:
            str: Result of the player's turn - 'bust', 'player', 'dealer', or 'tie'.
        """
        if action == 'hit':
            self.player.hand.append(self.deck.draw_card())
            self.logger.log(f'Player chose to hit. New hand: {self.player.hand}')
            if self.player.calculate_total() > 21:
                self.logger.log('Player busts')
                self.player.credits -= self.bet
                return 'bust'
        elif action == 'hold':
            self.player_turn_complete = True
            self.dealer.hand[1] = self.deck.draw_card()  # Reveal the hidden card
            while self.dealer.calculate_total() < 17:
                self.dealer.hand.append(self.deck.draw_card())
            dealer_total = self.dealer.calculate_total()
            player_total = self.player.calculate_total()
            if dealer_total > 21:
                self.logger.log('Dealer busts. Player wins.')
                self.player.credits += 2 * self.bet
                return 'player'
            elif dealer_total > player_total:
                self.logger.log('Dealer wins.')
                self.player.credits -= self.bet
                return 'dealer'
            elif dealer_total == player_total:
                self.logger.log('It\'s a tie.')
                self.player.credits += self.bet
                return 'tie'
            else:
                self.logger.log('Player wins.')
                self.player.credits += 2 * self.bet
                return 'player'

    def make_bet(self, bet_amount):
        """
        Sets the bet amount and starts a new game if the bet is valid.

        Args:
            bet_amount (int): The amount of money the player bets.

        Returns:
            None
        """
        if 0 < bet_amount <= self.player.credits:
            self.bet = bet_amount
            self.logger.log(f'Player placed a bet of {self.bet}')
            self.start_game()
        else:
            self.logger.log(f'Invalid bet amount: {bet_amount}')

    def restart_game(self):
        """
        Restarts the game by reinitializing the BlackjackGame instance.

        Args:
            None

        Returns:
            None
        """
        self.logger.log('Game restarted')
        self.__init__()  # Reinitialize the game for a new start
