# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: This is the core implementation of the Battleship game. The Game class manages the setup,
#              gameplay, and overall flow of the game. It uses other classes such as Board, Player, Ship,
#              and Logger to facilitate the game logic and maintain game state.

from Player import Player
from Ship import Ship
from Board import Board
from GLogger import Logger
import random


class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player("Player 1")
        self.logger = Logger("./game_log.txt")

    def setup(self):
        # Place ships randomly on the board
        ship_sizes = [5, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for size in ship_sizes:
            while True:
                try:
                    start = (random.randint(0, 9), random.randint(0, 9))
                    orientation = random.choice(['H', 'V'])
                    ship = Ship(size)
                    self.board.place_ship(ship, start, orientation)
                    break
                except ValueError:
                    continue

    def play_turn(self, coord):
        result = self.player.make_move(self.board, coord)
        self.logger.log_move(self.board, coord, result)
        return result

    def is_game_over(self):
        return self.board.is_all_ships_sunk()

    def run(self):
        self.setup()
        while not self.is_game_over():
            # Here, you would integrate the GUI interaction to get player input
            pass
        print("Game Over!")
