import tkinter as tk
from GUI import TicTacToeGUI

# Author: Sohaib Hussain
# Date: 2024-08-05
# Description: This script initializes the main window and starts the Tic-Tac-Toe GUI application.

if __name__ == '__main__':
    # Create the main application window
    root = tk.Tk()
    # Initialize the TicTacToeGUI with the root window
    app = TicTacToeGUI(root)
    # Start the Tkinter main event loop
    root.mainloop()
