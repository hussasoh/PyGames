# Author: Sohaib Hussain
# Date: 2024-08-05
# Description: Class to manage the game logic, including player turns, scoring, and game state.

from Board import Board
import random
import logging

class Game:
    def __init__(self):
        self.game_number = 1
        self.scores = {'X': 0, 'O': 0}
        logging.basicConfig(filename='./tic_tac_toe.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.start_new_game()

    def start_new_game(self):
        """Starts a new game, initializing the board and player settings."""
        self.board = Board()
        self.current_player = 'Player 1'
        self.winner = None
        self.players = {'Player 1': 'O', 'Player 2': 'X'}
        logging.info(f'============== New Game {self.game_number} ==================')
        self.board.log_board_state()

    def make_move(self, row, col):
        """Handles a move made by the current player.

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.

        Returns:
            str: A message indicating the result of the move.
        """
        if self.winner:
            logging.info(f'Attempted move by {self.current_player} but the game has already been won.')
            return f'Game already won by {self.winner}.'

        if self.board.make_move(row, col, self.players[self.current_player]):
            logging.info(f'{self.current_player} moved to ({row}, {col})')
            winner_symbol = self.board.check_winner()
            if winner_symbol:
                self.winner = [name for name, symbol in self.players.items() if symbol == winner_symbol][0]
                self.scores[winner_symbol] += 1
                logging.info(f'{self.winner} wins!')
                self.board.log_board_state()
                return f'{self.winner} ({winner_symbol}) wins!'
            if self.board.is_full():
                logging.info('The game is a draw.')
                self.board.log_board_state()
                return 'The game is a draw.'
            self.current_player = 'Player 1' if self.current_player == 'Player 2' else 'Player 2'
            logging.info(f'{self.current_player}\'s turn.')
            return f'{self.current_player}\'s turn.'
        else:
            logging.info(f'Invalid move by {self.current_player} to ({row}, {col})')
            return 'Invalid move. Try again.'

    def get_board(self):
        """Returns the current state of the game board.

        Returns:
            list: The game board as a 2D list.
        """
        return self.board.board

    def get_scores(self):
        """Returns the current scores of the players.

        Returns:
            dict: The scores of the players with their symbols as keys.
        """
        return self.scores

    def increment_game_number(self):
        """Increments the game number and starts a new game."""
        self.game_number += 1
        self.start_new_game()
