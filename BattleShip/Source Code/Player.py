# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: The Player class represents a player in the Battleship game. It keeps track of the player's name,
#              their moves, and provides functionality to make moves on the game board.

class Player:
    def __init__(self, name):
        """
        Initialize the player with a name and an empty list of moves.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.moves = []

    def make_move(self, board, coord):
        """
        Make a move by attacking the specified coordinates on the board.

        Args:
            board (Board): The game board where the move will be made.
            coord (tuple): The coordinates (row, col) to attack.

        Returns:
            str: The result of the attack, which can be 'Hit', 'Miss', or 'Already Attacked'.
        """
        # Validate the move and update the board
        result = board.receive_attack(coord)
        self.moves.append(coord)
        return result

