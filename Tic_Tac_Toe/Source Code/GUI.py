from Game import Game
import tkinter as tk
from tkinter import messagebox


# Author: Sohaib Hussain
# Date: 2024-08-05
# Description: GUI class for the Tic-Tac-Toe game, handling the user interface and interactions.
class TicTacToeGUI:
    def __init__(self, root):
        self.game = Game()
        self.root = root
        self.root.title('Tic-Tac-Toe')

        # Create a frame for the UI
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Create the board buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        """Initializes and places the widgets (labels, buttons) on the GUI."""
        # Player names and scores
        self.player1_label = tk.Label(self.frame, text='Player 1 (O)', font=('Arial', 16))
        self.player1_label.grid(row=0, column=0, padx=5, pady=5)

        self.player2_label = tk.Label(self.frame, text='Player 2 (X)', font=('Arial', 16))
        self.player2_label.grid(row=0, column=2, padx=5, pady=5)

        self.player1_score_label = tk.Label(self.frame, text='Score: 0', font=('Arial', 16))
        self.player1_score_label.grid(row=1, column=0, padx=5, pady=5)

        self.player2_score_label = tk.Label(self.frame, text='Score: 0', font=('Arial', 16))
        self.player2_score_label.grid(row=1, column=2, padx=5, pady=5)

        # Board buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame, text=' ', font=('Arial', 24), width=5, height=2,
                                   command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=2 + i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        # Info label
        self.info_label = tk.Label(self.frame, text='', font=('Arial', 16))
        self.info_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        # End Game button
        self.end_game_button = tk.Button(self.frame, text='End Game', font=('Arial', 16), command=self.end_game)
        self.end_game_button.grid(row=6, column=0, columnspan=3, pady=10)

        # Quit button
        self.quit_button = tk.Button(self.frame, text='Quit', font=('Arial', 16), command=self.quit_game)
        self.quit_button.grid(row=7, column=0, columnspan=3, pady=10)
        self.quit_button.config(state=tk.DISABLED)  # Initially disabled

        # Start the game automatically
        self.start_game()

    def start_game(self):
        """Starts a new game and updates the GUI accordingly."""
        self.game.start_new_game()
        self.update_player_info()
        self.info_label.config(text=f'{self.game.current_player}\'s turn.')

    def button_click(self, row, col):
        """Handles the click event for board buttons.

        Args:
            row (int): The row index of the button clicked.
            col (int): The column index of the button clicked.
        """
        if self.game.winner:
            return  # Ignore clicks if the game has already been won

        result = self.game.make_move(row, col)
        self.update_board()

        if 'wins' in result or 'draw' in result:
            self.update_scores()
            self.info_label.config(text=result)
            # Reset the board for the next game
            self.reset_board()
        else:
            self.info_label.config(text=result)

    def update_board(self):
        """Updates the GUI to reflect the current state of the game board."""
        board = self.game.get_board()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=board[i][j])

    def update_player_info(self):
        """Updates the player labels with their respective symbols."""
        self.player1_label.config(text=f'Player 1 (O)')
        self.player2_label.config(text=f'Player 2 (X)')
        self.update_scores()

    def update_scores(self):
        """Updates the scores displayed on the GUI."""
        scores = self.game.get_scores()
        self.player1_score_label.config(text=f'Score: {scores["O"]}')
        self.player2_score_label.config(text=f'Score: {scores["X"]}')

    def reset_board(self):
        """Resets the board for a new game and updates the GUI."""
        # Reset the buttons for a new game
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')
        # Start a new game automatically
        self.start_game()

    def end_game(self):
        """Ends the current game and displays the final scores."""
        final_scores = self.game.get_scores()
        self.info_label.config(
            text=f'Final Scores:\nPlayer 1 (O): {final_scores["O"]}\nPlayer 2 (X): {final_scores["X"]}')
        self.end_game_button.config(state=tk.DISABLED)
        self.quit_button.config(state=tk.NORMAL)

    def quit_game(self):
        """Exits the game."""
        self.root.quit()