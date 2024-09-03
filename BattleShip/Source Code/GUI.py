# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: The BattleshipGUI class provides a graphical user interface (GUI) for the Battleship game.
#              It utilizes the tkinter library to create the main window, a grid for the game board,
#              and input controls for player actions. The GUI handles user interactions and updates the
#              game state accordingly, including a timer to track the duration of the game.

import tkinter as tk
from tkinter import messagebox
from BattleshipGame import Game
import time


class BattleshipGUI:
    def __init__(self, root):
        """
        Initialize the BattleshipGUI with a root window and setup the game.

        Args:
            root (tk.Tk): The root window for the tkinter application.
        """
        self.game = Game()
        self.game.setup()
        self.root = root
        self.root.title("Battleship Game")

        # Timer variables
        self.start_time = time.time()
        self.timer_label = None

        # Configure grid layout with some padding
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Create a frame for the board and set some padding
        self.board_frame = tk.Frame(root, padx=10, pady=10)
        self.board_frame.grid(row=0, column=0, sticky='nsew')

        # Setup board with larger buttons
        self.setup_board()

        # Create a frame for controls
        self.controls_frame = tk.Frame(root, padx=10, pady=10)
        self.controls_frame.grid(row=1, column=0, sticky='ew')

        # Message label for instructions
        self.message_label = tk.Label(self.controls_frame, text="Enter coordinates (row, col):", font=("Arial", 14))
        self.message_label.grid(row=0, column=0, pady=10)

        # Entry widget for coordinates input with a larger font
        self.entry = tk.Entry(self.controls_frame, font=("Arial", 14), width=10)
        self.entry.grid(row=0, column=1, pady=10)

        # Attack button with a larger font
        self.attack_button = tk.Button(self.controls_frame, text="Attack", font=("Arial", 14), command=self.attack)
        self.attack_button.grid(row=0, column=2, pady=10, padx=10)

        # Timer label
        self.timer_label = tk.Label(root, text="Time: 0:00", font=("Arial", 14))
        self.timer_label.grid(row=2, column=0, sticky='se', padx=10, pady=10)
        self.update_timer()

    def setup_board(self):
        """
        Setup the game board with a grid of buttons.

        Each button represents a cell on the game board and is initially marked with a '-'.
        The buttons are arranged in a 10x10 grid.
        """
        self.buttons = []
        for i in range(10):
            row = []
            for j in range(10):
                btn = tk.Button(self.board_frame, text='-', font=("Arial", 14), width=4, height=2,
                                command=lambda i=i, j=j: self.on_click(i, j))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def on_click(self, row, col):
        """
        Handle the event when a board cell is clicked.

        This method updates the entry widget with the coordinates of the clicked cell.

        Args:
            row (int): The row index of the clicked cell.
            col (int): The column index of the clicked cell.
        """
        # Highlight the selected cell in the entry box
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{row + 1},{col + 1}")

    def attack(self):
        """
        Handle the attack action based on the coordinates entered by the player.

        This method processes the attack, updates the game board, and checks the game's status.
        It also handles invalid inputs and displays appropriate messages.
        """
        try:
            coord = tuple(map(lambda x: int(x) - 1, self.entry.get().split(',')))
            if not (0 <= coord[0] < 10 and 0 <= coord[1] < 10):
                raise ValueError
            result = self.game.play_turn(coord)
            self.update_board()
            if result == 'Hit':
                self.buttons[coord[0]][coord[1]].config(text='X', bg='red')
            elif result == 'Miss':
                self.buttons[coord[0]][coord[1]].config(text='O', bg='blue')
            elif result == 'Already Attacked':
                messagebox.showinfo("Invalid Move", "This position has already been attacked.")
            if self.game.is_game_over():
                self.handle_end_of_game()
        except (ValueError, IndexError):
            messagebox.showinfo("Invalid Input", "Please enter valid coordinates in the format 'row,col'.")

    def update_board(self):
        """
        Update the visual representation of the game board.

        This method refreshes the board display to show hits (marked as 'X' in red)
        and misses (marked as 'O' in blue) based on the game's current state.
        """
        for row in range(10):
            for col in range(10):
                if self.game.board.grid[row][col] == 'X':
                    self.buttons[row][col].config(text='X', bg='red')
                elif self.game.board.grid[row][col] == 'O':
                    self.buttons[row][col].config(text='O', bg='blue')

    def update_timer(self):
        """
        Update the timer label to show the elapsed time.

        This method updates the timer label every second to reflect the time elapsed since the game started.
        """
        elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        self.timer_label.config(text=f"Time: {minutes}:{seconds:02}")
        self.root.after(1000, self.update_timer)

    def handle_end_of_game(self):
        """
        Handle the end of the game.

        This method shows a message box with the game result and logs the game duration.
        """
        elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        game_duration = f"{minutes}:{seconds:02}"

        messagebox.showinfo("Game Over", f"All ships have been sunk!\nTime taken: {game_duration}")
        self.game.logger.log_move(self.game.board, None, "Game Over")
        self.game.logger.log_entry(f"Game duration: {game_duration}")
        self.root.quit()
