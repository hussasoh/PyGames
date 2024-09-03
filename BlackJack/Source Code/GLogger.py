# Author: Sohaib Hussain
# Date: August 6, 2024
# Description: This class handles logging for the Blackjack game.
# It manages the creation of a logger, the configuration of log file handling,
# and provides a method to log messages at the INFO level.

import logging

class GameLogger:
    def __init__(self, filename="./game_log.txt"):
        """
        Initializes the GameLogger with a file handler to write logs to a specified file.

        Args:
            filename (str): The name of the file where logs will be written. Defaults to "./game_log.txt".

        Returns:
            None
        """
        self.logger = logging.getLogger("BlackjackGameLogger")
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log(self, message):
        """
        Logs a message with INFO level.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        self.logger.info(message)
