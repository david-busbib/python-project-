import tkinter as tk
from boggle_board_randomizer import randomize_board
from GUI import *


root = tk.Tk()
root.title("Boogle")
#root.resizable(False, False)
a = BoardGUI(root)
# b= Startframe()
# a.grid(row=0)
# a.forget()
# b.grid()
a.root.mainloop()