# Author: Sohaib Hussain
# Date: 2024-08-05
# Description: Class to manage the game board's state, moves, and checks for winning conditions.
import logging

class Board:
    def __init__(self):
        logging.basicConfig(filename='./tic_tac_toe.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.initialize_board()

    def initialize_board(self):
        """Initializes or resets the game board and move log."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.move_log = []
        self.log_board_state()

    def make_move(self, row, col, player):
        """Attempts to place a player's move on the board.

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.
            player (str): The player's symbol ('X' or 'O').

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            self.move_log.append((row, col, player))
            self.log_board_state()
            return True
        return False

    def check_winner(self):
        """Checks if there's a winner on the board.

        Returns:
            str or None: The symbol of the winning player ('X' or 'O'), or None if no winner.
        """
        lines = [self.board[i] for i in range(3)] + \
                [[self.board[i][j] for i in range(3)] for j in range(3)] + \
                [[self.board[i][i] for i in range(3)]] + \
                [[self.board[i][2 - i] for i in range(3)]]

        for line in lines:
            if line[0] != ' ' and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_full(self):
        """Checks if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != ' ' for row in self.board for cell in row)

    def log_board_state(self):
        """Logs the current state of the board to a log file."""
        board_state = '\n'.join([' '.join(row) for row in self.board])
        logging.info(f'Board state:\n{board_state}\n')
