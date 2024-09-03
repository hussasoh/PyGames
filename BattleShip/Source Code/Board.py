# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: The Board class represents the game board for the Battleship game. It manages the grid,
#              the placement of ships, tracking hits and misses, and provides functionality to check
#              for valid positions and handle attacks.

import random

class Board:
    def __init__(self, size=10):
        """
        Initialize the game board with a given size.

        Args:
            size (int): The size of the board (default is 10x10).
        """
        self.size = size
        self.grid = [['-' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.hits = []
        self.misses = []

    def place_ship(self, ship, start, orientation):
        """
        Place a ship on the board at the specified start position and orientation.

        Args:
            ship (Ship): The ship to place.
            start (tuple): The starting position (row, col) for the ship.
            orientation (str): The orientation of the ship, 'H' for horizontal, 'V' for vertical.

        Raises:
            ValueError: If the ship cannot be placed at the specified location.
        """
        ship.place(start, orientation)
        for pos in ship.positions:
            if self.is_valid_position(pos):
                self.grid[pos[0]][pos[1]] = 'S'
            else:
                raise ValueError("Invalid position for ship placement")
        self.ships.append(ship)

    def is_valid_position(self, pos):
        """
        Check if a position is valid for placing a ship.

        A position is valid if it is within the board boundaries and does not overlap with
        existing ships.

        Args:
            pos (tuple): The position (row, col) to check.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        row, col = pos
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        for ship in self.ships:
            if pos in ship.positions:
                return False
        return True

    def receive_attack(self, coord):
        """
        Handle an attack at the specified coordinates.

        Args:
            coord (tuple): The coordinates (row, col) of the attack.

        Returns:
            str: 'Hit' if a ship is hit, 'Miss' if no ship is at the location,
                 'Already Attacked' if the position was already attacked.
        """
        row, col = coord
        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            self.hits.append(coord)
            for ship in self.ships:
                if ship.check_hit(coord):
                    return 'Hit'
        elif self.grid[row][col] == '-':
            self.grid[row][col] = 'O'
            self.misses.append(coord)
            return 'Miss'
        return 'Already Attacked'

    def is_all_ships_sunk(self):
        """
        Check if all ships on the board have been sunk.

        Returns:
            bool: True if all ships are sunk, False otherwise.
        """
        return all(ship.is_sunk for ship in self.ships)

    def display(self, show_ships=False):
        """
        Display the current state of the board.

        Args:
            show_ships (bool): If True, reveal the positions of the ships.
                               If False, hide the ships and only show hits and misses.
        """
        for row in self.grid:
            print(" ".join(row))
