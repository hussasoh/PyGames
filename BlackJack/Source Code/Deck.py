# Author: Sohaib Hussain
# Date: August 6, 2024
# Description: This class represents a deck of cards used in a Blackjack game.
# It handles deck creation, shuffling, and drawing cards.

from Card import Card
import random

class Deck:
    def __init__(self):
        """
        Initializes the Deck by creating and shuffling a deck of cards.

        Args:
            None

        Returns:
            None
        """
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        """
        Creates a deck of 52 cards with values from 1 to 13 for each of the four suits.

        Args:
            None

        Returns:
            list: A list of card values representing the deck.
        """
        return [value for value in range(1, 14)] * 4

    def shuffle(self):
        """
        Shuffles the deck of cards.

        Args:
            None

        Returns:
            None
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draws a card from the deck.

        Args:
            None

        Returns:
            int: The value of the drawn card.

        Raises:
            ValueError: If there are no cards left in the deck.
        """
        if len(self.cards) == 0:
            raise ValueError("No cards left in the deck")
        return self.cards.pop()
