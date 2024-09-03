import tkinter as tk
from GUI import GameUI

def main():
    root = tk.Tk()
    app = GameUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
