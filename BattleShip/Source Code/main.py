# Author: Sohaib Hussain
# Date: August 5, 2024
# Description: The main entry point for running the Battleship game GUI. 
#              It initializes the Tkinter application window and starts the GUI event loop.

from GUI import BattleshipGUI
import tkinter as tk

if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()

    # Initialize the Battleship game GUI
    app = BattleshipGUI(root)

    # Run the Tkinter event loop
    root.mainloop()
