import tkinter as tk
from tkinter import simpledialog, messagebox
from BlackjackGame import BlackjackGame  # Ensure this import matches your file structure


# Author: Sohaib Hussain
# Date: August 6, 2024
# Description: This class provides the graphical user interface for the Blackjack game.
# It includes methods to handle user interactions such as making bets, hitting, standing,
# and restarting the game. It also updates the GUI to reflect the current state of the game.

class BlackjackGUI:
    def __init__(self, root):
        """
        Initializes the GUI, sets up the main window, and starts the game.

        Args:
            root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Blackjack")
        self.game = BlackjackGame()
        self.create_widgets()
        self.update_info()

    def create_widgets(self):
        """
        Creates and places the GUI widgets such as labels, buttons, and frames.
        """
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(padx=10, pady=10)

        # Title
        self.title_label = tk.Label(main_frame, text="Welcome to Blackjack!", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=(0, 20))

        # Info display
        self.info_frame = tk.Frame(main_frame)
        self.info_frame.pack(pady=(0, 20))

        self.info_label = tk.Label(self.info_frame, text="", font=("Helvetica", 14))
        self.info_label.grid(row=0, column=0, columnspan=2, sticky="w")

        # Action buttons
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=(0, 20))

        self.bet_button = tk.Button(button_frame, text="Make a Bet", command=self.make_bet, width=15, height=2,
                                    font=("Helvetica", 12))
        self.bet_button.grid(row=0, column=0, padx=5)

        self.hit_button = tk.Button(button_frame, text="Hit", command=self.hit, width=15, height=2,
                                    font=("Helvetica", 12))
        self.hit_button.grid(row=0, column=1, padx=5)

        self.stand_button = tk.Button(button_frame, text="Stand", command=self.stand, width=15, height=2,
                                      font=("Helvetica", 12))
        self.stand_button.grid(row=0, column=2, padx=5)

        self.restart_button = tk.Button(button_frame, text="Restart", command=self.restart, width=15, height=2,
                                        font=("Helvetica", 12))
        self.restart_button.grid(row=1, column=0, columnspan=3, pady=(10, 0))

    def make_bet(self):
        """
        Prompts the user to enter a bet amount and starts a new game with that bet.
        """
        bet = simpledialog.askinteger("Bet", "Enter your bet:", minvalue=1, maxvalue=self.game.player.credits)
        if bet is not None:
            self.game.bet = bet
            self.game.start_game()
            self.update_info()
        else:
            messagebox.showerror("Invalid Bet", "Bet must be within the available credits.")

    def hit(self):
        """
        Handles the player's action to hit. Updates the game state and GUI accordingly.
        """
        result = self.game.player_turn('hit')
        if result == 'bust':
            messagebox.showinfo("Game Over", "You busted! Dealer wins.")
            self.game.player.credits -= self.game.bet
            self.update_info()
        else:
            self.update_info()

    def stand(self):
        """
        Handles the player's action to stand. Finalizes the game state and updates the GUI.
        """
        result = self.game.player_turn('hold')
        if result == 'bust':
            messagebox.showinfo("Game Over", "You busted! Dealer wins.")
        elif result == 'player':
            messagebox.showinfo("Game Over", "You win!")
        elif result == 'dealer':
            messagebox.showinfo("Game Over", "Dealer wins!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
        self.update_info()

    def restart(self):
        """
        Restarts the game if the player has credits left; otherwise, ends the game.
        """
        if self.game.player.credits > 0:
            self.game = BlackjackGame()
            self.update_info()
        else:
            messagebox.showinfo("Game Over", "No credits left. Game Over.")
            self.root.quit()

    def update_info(self):
        """
        Updates the GUI to display the current state of the game including hands and totals.
        """

        def card_str(card):
            """
            Converts a card value to a string representation.

            Args:
                card (int): The card value (1 to 13).

            Returns:
                str: The string representation of the card.
            """
            if card == 1:
                return 'A'
            elif card == 11:
                return 'J'
            elif card == 12:
                return 'Q'
            elif card == 13:
                return 'K'
            else:
                return str(card)

        player_hand = ', '.join(card_str(card) for card in self.game.player.hand)
        player_total = self.game.player.calculate_total()

        # Determine dealer hand display
        dealer_hand_display = ', '.join(card_str(card) for card in self.game.dealer.hand)
        dealer_total = self.game.dealer.calculate_total()

        # Only show the second card if the player has finished their turn
        if self.game.player_turn_complete:
            # Reveal the dealer's face-down card
            if len(self.game.dealer.hand) > 1 and self.game.dealer.hand[1] is None:
                dealer_hand_display = f"{card_str(self.game.dealer.hand[0])}, {card_str(self.game.dealer.hand[1])}"
        else:
            # Hide the dealer's second card
            dealer_hand_display = f"{card_str(self.game.dealer.hand[0])}, X"

        self.info_label.config(text=f"Player Credits: {self.game.player.credits}\n"
                                    f"Player Hand: {player_hand}\n"
                                    f"Player Total: {player_total}\n\n"
                                    f"Dealer Hand: {dealer_hand_display}\n"
                                    f"Dealer Total: {dealer_total}")
