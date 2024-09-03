# Author: Sohaib Hussain
# Date: August 6, 2024
# Description: This class represents the dealer in a Blackjack game.
# It extends the Player class and provides functionality specific to the dealer,
# including automatically playing the dealer's turn according to Blackjack rules.

from Player import Player

class Dealer(Player):
    def __init__(self):
        """
        Initializes the Dealer with zero credits and inherits from the Player class.

        Args:
            None

        Returns:
            None
        """
        super().__init__(credits=0)

    def play(self, deck):
        """
        Executes the dealer's turn according to Blackjack rules:
        The dealer will keep drawing cards until the total is 17 or higher.

        Args:
            deck (Deck): The deck of cards from which to draw.

        Returns:
            None
        """
        while self.calculate_total() < 17:
            self.draw_card(deck)
