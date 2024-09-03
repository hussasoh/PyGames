# Author: Sohaib Hussain
# Date: August 6, 2024
# Description: This class represents a player in the Blackjack game.
# It handles the player's credits, the player's hand, and calculates the total value of the hand.

from Card import Card


class Player:
    def __init__(self, credits=50):
        """
        Initializes a player with a specified number of credits and an empty hand.

        Args:
            credits (int): The initial number of credits for the player. Defaults to 50.

        Returns:
            None
        """
        self.credits = credits
        self.hand = []

    def calculate_total(self):
        """
        Calculates the total value of the player's hand, taking into account the value of aces.

        Returns:
            int: The total value of the player's hand.
        """
        total = 0
        aces = 0
        for card in self.hand:
            if card is None:
                continue  # Skip None values
            if card in [11, 12, 13]:
                total += 10
            elif card == 1:
                aces += 1
                total += 11
            else:
                total += card
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total
