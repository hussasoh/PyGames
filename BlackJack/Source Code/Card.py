# Author: Sohaib Hussain
# Date: August 6, 2024
# Description: This class represents a playing card in a deck of cards used for Blackjack.
# It includes card suits and values, and provides methods for initialization and representation.

import random


class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'J': 11, 'Q': 12, 'K': 13, 'A': 1}

    def __init__(self, value, suit):
        """
        Initializes a card with a given value and suit.

        Args:
            value (str): The value of the card (e.g., '2', 'A').
            suit (str): The suit of the card (e.g., 'Hearts', 'Spades').

        Returns:
            None
        """
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Provides a string representation of the card.

        Returns:
            str: A string representation of the card in the format "ValueSuitInitial".
        """
        return f"{self.value}{self.suit[0]}"
