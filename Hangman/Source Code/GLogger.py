import datetime


# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: This class provides logging functionalities for the Hangman game.
# It handles logging game events such as starting a new game, making guesses,
# restarting the game, and ending the game. All logs are saved to a file.

class GameLogger:
    @staticmethod
    def log_entry(entry):
        """
        Appends a log entry to the game log file.

        Parameters:
        entry (str): The log entry to be written to the file.
        """
        with open('./game_log.txt', 'a') as f:
            f.write(entry + '\n')

    @staticmethod
    def start_new_game(word):
        """
        Logs the start of a new game session, including the target word.

        Parameters:
        word (str): The word to be guessed in the new game.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        GameLogger.log_entry(f"\n--- New Game Started: {timestamp} ---")
        GameLogger.log_entry(f"Word to guess: {word}")

    @staticmethod
    def log_guess(letter, lives_remaining):
        """
        Logs a player's guess and the number of lives remaining.

        Parameters:
        letter (str): The letter guessed by the player.
        lives_remaining (int): The number of lives remaining after the guess.
        """
        GameLogger.log_entry(f"Guess: {letter}, Lives Remaining: {lives_remaining}")

    @staticmethod
    def log_restart():
        """
        Logs the event of restarting the game.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        GameLogger.log_entry(f"Game Restarted: {timestamp}")

    @staticmethod
    def log_game_over(word_was_guessed):
        """
        Logs the outcome of the game, indicating whether the player guessed the word or ran out of lives.

        Parameters:
        word_was_guessed (bool): True if the player guessed the word, False if they ran out of lives.
        """
        if word_was_guessed:
            GameLogger.log_entry("Game Over: Player guessed the word!")
        else:
            GameLogger.log_entry("Game Over: Player ran out of lives!")
