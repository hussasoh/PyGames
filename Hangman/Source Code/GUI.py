import tkinter as tk
from tkinter import messagebox
from HangmanGame import HangmanGame
from GLogger import GameLogger


# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: This script implements a graphical user interface (GUI) for the Hangman game using tkinter.
# The game includes a virtual keyboard and tracks game progress and actions through detailed logging.

class GameUI:
    def __init__(self, root):
        """
        Initializes the game UI and starts a new game session.
        Sets up the main window, labels, and keyboard.
        """
        self.game = HangmanGame()  # Create a new Hangman game instance
        self.root = root  # Reference to the main application window
        self.root.title("Hangman Game")  # Set the title of the window
        self.create_widgets()  # Create and place all the widgets in the window
        GameLogger.start_new_game(self.game.word)  # Log the word to guess for the new game

    def create_widgets(self):
        """
        Creates and arranges all widgets in the main window.
        This includes labels, keyboard buttons, and the restart button.
        """
        self.word_label = tk.Label(self.root, text=self.game.get_word_display(), font=('Arial', 24), bg='white', width=30)
        self.word_label.pack(pady=10)  # Display the current state of the word with placeholders

        self.lives_label = tk.Label(self.root, text=f"Lives remaining: {self.game.get_lives()}", font=('Arial', 18))
        self.lives_label.pack(pady=10)  # Display the number of lives remaining

        self.keyboard_frame = tk.Frame(self.root)
        self.keyboard_frame.pack(pady=10)  # Create and place a frame for the virtual keyboard

        self.buttons = {}  # Dictionary to hold references to keyboard buttons
        self.create_keyboard()  # Create and place keyboard buttons

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=('Arial', 18))
        self.restart_button.pack(pady=10)  # Create and place the restart button

    def create_keyboard(self):
        """
        Creates buttons for each letter of the alphabet and places them in a grid.
        The buttons allow the player to make guesses by clicking on them.
        """
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for letter in letters:
            button = tk.Button(self.keyboard_frame, text=letter, font=('Arial', 18), width=3, height=2,
                               command=lambda l=letter: self.process_guess(l))
            button.grid(row=letters.index(letter) // 9, column=letters.index(letter) % 9)
            self.buttons[letter] = button  # Store the button reference for later use

    def process_guess(self, letter):
        """
        Handles a letter guess from the player. Updates the game state and UI.
        Logs the guess and remaining lives.
        """
        if self.game.is_game_over():
            return  # Do nothing if the game is already over
        if not letter.isalpha() or len(letter) != 1:
            return  # Ignore invalid inputs
        correct = self.game.make_guess(letter)  # Process the guess
        self.update_ui()  # Update the UI with the new game state
        GameLogger.log_guess(letter, self.game.get_lives())  # Log the guess and remaining lives
        if self.game.is_game_over():
            self.handle_end_of_game()  # Handle end of game scenarios

    def update_ui(self):
        """
        Updates the user interface to reflect the current game state.
        """
        self.word_label.config(text=self.game.get_word_display())  # Update the word display
        self.lives_label.config(text=f"Lives remaining: {self.game.get_lives()}")  # Update lives display
        self.update_keyboard()  # Update the keyboard buttons (disable used letters)

    def update_keyboard(self):
        """
        Updates the virtual keyboard buttons to reflect the letters that have been guessed.
        Disables and greys out buttons for guessed letters.
        """
        for letter, button in self.buttons.items():
            if letter in self.game.guesses:
                button.config(state=tk.DISABLED, bg='lightgrey')  # Disable and grey out used letters
            else:
                button.config(state=tk.NORMAL, bg='SystemButtonFace')  # Enable and reset color for unused letters

    def handle_end_of_game(self):
        """
        Handles the end of the game. Shows a message box with the result and logs the game outcome.
        """
        if '_' not in self.game.get_word_display():
            messagebox.showinfo("Congratulations!", "You guessed the word!")  # Player won
            GameLogger.log_game_over(word_was_guessed=True)  # Log game outcome
        else:
            messagebox.showinfo("Game Over", "You ran out of lives!")  # Player lost
            GameLogger.log_game_over(word_was_guessed=False)  # Log game outcome
        self.restart_game()  # Restart the game

    def restart_game(self):
        """
        Restarts the game by resetting the game state and logging the restart.
        """
        GameLogger.log_restart()  # Log game restart
        self.game.reset_game()  # Reset game state
        GameLogger.start_new_game(self.game.word)  # Log the new word to guess
        self.update_ui()  # Update the UI for the new game

