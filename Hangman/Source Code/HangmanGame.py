import random


# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: This class implements the logic for the Hangman game.
# It handles game initialization, making guesses, tracking lives, and determining the end of the game.

class HangmanGame:
    def __init__(self):
        """
        Initializes the game with a predefined list of words and resets the game state.
        """
        self.words = ["programming", "development", "python", "algorithm", "exception"]
        self.reset_game()  # Start a new game session

    def reset_game(self):
        """
        Resets the game to its initial state with a new word, empty guesses, full lives, and game not over.
        """
        self.word = random.choice(self.words).upper()  # Randomly choose a word from the list
        self.guesses = set()  # Set to store guessed letters
        self.lives = 5  # Initial number of lives
        self.game_over = False  # Game is not over at the start
        self.word_display = ['_'] * len(self.word)  # Display underscores for each letter in the word
        self.log = []  # List to store game logs

    def make_guess(self, letter):
        """
        Processes a player's guess, updates the game state, and logs the outcome.

        Parameters:
        letter (str): The letter guessed by the player.

        Returns:
        bool: True if the guess was correct, False otherwise.
        """
        if self.game_over:
            return False  # Do nothing if the game is already over

        letter = letter.upper()  # Normalize the letter to uppercase

        if letter in self.guesses:
            return False  # Letter already guessed

        self.guesses.add(letter)  # Add the guessed letter to the set of guesses

        if letter in self.word:
            # Update word_display with correct guesses
            for i, char in enumerate(self.word):
                if char == letter:
                    self.word_display[i] = letter
            if '_' not in self.word_display:
                self.game_over = True  # Player has guessed the word
                self.log.append(f"Correct guess! The word was: {self.word}")
            return True  # Guess was correct
        else:
            self.lives -= 1  # Decrement lives for incorrect guess
            if self.lives <= 0:
                self.game_over = True  # Game over due to no lives left
                self.log.append(f"Game Over! The word was: {self.word}")
            return False  # Guess was incorrect

    def get_word_display(self):
        """
        Returns the current display of the word with guessed letters and underscores.

        Returns:
        str: The word display with spaces between letters.
        """
        return ' '.join(self.word_display)

    def get_lives(self):
        """
        Returns the number of lives remaining.

        Returns:
        int: The number of lives left.
        """
        return self.lives

    def is_game_over(self):
        """
        Checks if the game is over.

        Returns:
        bool: True if the game is over, False otherwise.
        """
        return self.game_over

    def get_log(self):
        """
        Returns the log of game events.

        Returns:
        list: A list of strings with game events.
        """
        return self.log
