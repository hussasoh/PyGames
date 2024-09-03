# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: The Logger class handles logging of game moves and board state to a specified file.
#              It provides functionality to record each move made by the player along with the result
#              and the current state of the game board.

class Logger:
    def __init__(self, file_path):
        """
        Initialize the logger with the path to the log file.

        Args:
            file_path (str): The path to the file where logs will be saved.
        """
        self.file_path = file_path



    def log_move(self, board, coord, result):
        """
        Log a move to the file, including the coordinates of the move,
        the result of the move, and the current state of the board.

        Args:
            board (Board): The game board to log.
            coord (tuple): The coordinates (row, col) of the move.
            result (str): The result of the move, which can be 'Hit', 'Miss', or 'Already Attacked'.
        """
        with open(self.file_path, 'a') as file:
            file.write(f"Move: {coord}, Result: {result}\n")
            self.log_board(board)

    def log_board(self, board):
        """
        Log the current state of the board to the file.

        Args:
            board (Board): The game board to log.
        """
        with open(self.file_path, 'a') as file:
            for row in board.grid:
                file.write(" ".join(row) + "\n")
            file.write("\n")

    def log_entry(self, entry):
        """
        Log a general entry to the file. This can be used to record additional information such as
        game duration or other notable events.

        Args:
            entry (str): The entry to be logged. This can be any relevant string.
        """
        with open(self.file_path, 'a') as file:
            file.write(f"{entry}\n")
