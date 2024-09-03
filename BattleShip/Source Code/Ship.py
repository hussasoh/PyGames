# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: The Ship class represents a ship in the Battleship game. It includes the size of the ship,
#              its positions on the board, and whether it has been sunk. It also provides methods for
#              placing the ship on the board and checking if it has been hit.

class Ship:
    def __init__(self, size):
        self.size = size
        self.positions = []  # List of tuples (row, col)
        self.is_sunk = False

    def place(self, start, orientation):
        """
        Calculate ship positions based on the starting point and orientation.

        Args:
            start (tuple): Starting coordinate (row, col).
            orientation (str): 'H' for horizontal or 'V' for vertical orientation.

        """
        row, col = start
        if orientation == 'H':  # Horizontal
            self.positions = [(row, col + i) for i in range(self.size)]
        elif orientation == 'V':  # Vertical
            self.positions = [(row + i, col) for i in range(self.size)]

    def check_hit(self, coord):
        """
        Check if the ship is hit at the given coordinate.

        Args:
            coord (tuple): Coordinate (row, col) to check for a hit.

        Returns:
            bool: True if the ship is hit, False otherwise.

        """
        if coord in self.positions:
            self.positions.remove(coord)
            if not self.positions:
                self.is_sunk = True
            return True
        return False

