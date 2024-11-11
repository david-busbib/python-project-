"""
Names: Yogev Shapira, David Busbib
Usernames: yogev.shapira,dbusbib123
ID's: 213032576, 336224076
File: snake_main.py
Students we discussed the exe with: Bezalel Yanir, Oryan Hassidim
Web pages we used:
"""


import tkinter as tk
from boogle_Board import Board
from tkinter import messagebox

from copy import deepcopy
from tkinter import *
from tkinter.font import Font
BUTTON_COLOR = "#00ffff"
BUTTON_CLICKED = 'gray'
COLOR = '#00aead'
TIME_TEXT = "Time left: 03:00"
TIME = 1*60*1000
BACKGROUND_COLOR = 'yellow'
PASS_COLLOR ='orange'
IMAGE_PATH = 'boogle.photo.png'
WIDTH, HEIGHT = 600, 500
Font_1 = ("Comic Sans MS", 12, "bold")


class BoardGUI():
    """class initializes the graphic structure of the game boggle"""
    def __init__(self,root):
        self.root = root

        self.root.geometry("500x300")
        self.img = PhotoImage(file="boogle.photo.png")
        self.root.configure(bg=COLOR)
        self.root.resizable(False, False)

        self.open_screen()


    def open_screen(self):
        """creates initial screen that offers to run game"""
        """self.img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        self.lbl = tk.Label(self.root, image=self.img)
        self.lbl.img = self.img  # Keep a reference in case this code put is in a function.
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')"""
        self.img=PhotoImage(file="boogle.photo.png")

        self.open_frame = tk.Frame(self.root)
        self.sub_open_frame = tk.Frame(self.open_frame)
        self.open_frame.grid()
        self.sub_open_frame.grid(row=12, column=4)
        TEXT = "Welcome to Boogle Game!\n press on role to see the role\npress  start to start the game"
        self.open_message = tk.Label(text=TEXT,bg= 'black',font=Font_1
                                     ,image=self.img,
                                     compound='center',fg='blue',relief="sunken")
        self.open_message.grid(row =2,columnspan=2)
        self.help_botton =tk.Button(self.open_frame, text="HOW TO PLAY", bg=BUTTON_COLOR,
                                   width=15, height= 1, command=self.role,font=("Comic Sans MS", 11,'bold'))
        self.help_botton.grid(row= 11, column=7)
        self.start_btn = tk.Button(self.open_frame, text="PLAY", bg=BUTTON_COLOR,font=("Comic Sans MS", 11,'bold'),
                                   width=15, height= 1,
                            command=lambda:[self.start_game(),
                                            self.open_message.destroy(),
                                            self.start_btn.destroy(),self.open_frame.destroy()])
        self.start_btn.grid(row= 11, column=8)

    def start_game(self):
        """initializes all labels, buttons and board who are needed for running
         the game"""
        self.root.geometry("650x500")
        self.boogle_code = Board()
        self.type ={}
        self.buttons = {}
        self.frame = tk.Frame(self.root, bg=COLOR)
        self.sub_frame = tk.Frame(self.frame)
        self.frame.grid()
        self.sub_frame.grid(row=4, column=4)
        self.time = TIME

        self.used_words = tk.Label(self.frame, text="", bg=BACKGROUND_COLOR, width=18, height=17, relief=RIDGE,
                                   font=("Comic Sans MS", 11,'bold'))
        self.score_label = tk.Label(self.frame, text='Score: {}'.format(0), font=("Comic Sans MS", 20,'bold'),
                                    bg=BACKGROUND_COLOR,
                                    relief=SUNKEN,
                                    width=15, height=2)
        self.time_label = tk.Label(self.frame, text=TIME_TEXT, font=("Comic Sans MS", 20,'bold'),
                                   bg=BACKGROUND_COLOR, width=24,
                                   height=2,relief=SUNKEN)
        self.current_word = tk.Label(self.frame, text='', bg=BACKGROUND_COLOR, width=20, height=2, relief=RIDGE,
                                     font=("Comic Sans MS", 10,'bold')
                                    )

        self.score_label.grid(row=0, column=0, columnspan=2)
        self.time_label.grid(row=0, column=4, columnspan=8)
        self.buttons_frame()
        self.current_word.grid(row=1, column=0, columnspan=3,rowspan=2)

        self.used_words.grid(row=4, column=0, columnspan=4, rowspan=5)


        self.check_word_1 = tk.Button(self.frame, font=("Comic Sans MS", 12,'bold'), command=self.check_word
                                      , width=12, height=1,
                                    bg=BACKGROUND_COLOR, text='check word')
        self.check_word_1.grid(row=5, column=len(self.boogle_code.get_board()[0]) + 1, rowspan=4, columnspan=4)
        self.root.after(1000, self.update_time)


    def buttons_frame(self):
        board = deepcopy(self.boogle_code.get_board())
        for i in range(len(board)):
            for j in range(len(board[0])):
                current_button = tk.Button(self.sub_frame,
                text=board[i][j], bg= BUTTON_COLOR,font=("tahoma", 20, "bold"),
                 height=1,width=3, borderwidth=2, relief = "raised",
                command=lambda i=i, j=j: self.checker(i,j))
                current_button.grid(row=i, column=j + 0)
                board[i][j] = current_button

                self.buttons[(i,j)]= current_button
                current_button.grid(row=i + 3, column=j + 0)
                current_button.bind("<Enter>", lambda event, b=(i, j): self.touch_letter(b, True))
                current_button.bind("<Leave>", lambda event, b=(i, j),: self.touch_letter(b, False))
                self.type[(i, j)] = current_button

    def touch_letter(self, cord, flag):
        if flag:
            if self.type[(cord[0], cord[1])]['bg'] != PASS_COLLOR:
                self.type[(cord[0], cord[1])].configure(bg='white', fg="black")
        else:
            if self.type[(cord[0], cord[1])]['bg'] != PASS_COLLOR:
                self.type[(cord[0], cord[1])].configure(background=BUTTON_COLOR, fg="black")
    def role(self):
        ROLE = '''Game rules:\nYou have 3 minutes to find as many words as you can on the board.\n
        1.Every word grants square score of the path length.\n
        2.You can only get one score on each word, even if it appears several times on board.\n
        3. A neighbour letter is adjacent to current letter with 8 directions (up, down, right, left and 4 diagonals).\n
        4. In one path same cube cannot be used twice.\n
        That’s all! Enjoy!'''
        self.role = messagebox.showinfo('ROLE',ROLE)

    def checker(self,i,j):
        """get coordinates of pressed cell button and if signals it as pressed
        if this cell is legal as a path of creating word.
        label of showing written word is updated."""
        directions = [(i,j+1),  (i+1,j),  (i-1,j),  (i,j-1),
                      (i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]
        if len(self.boogle_code.get_path()) == 0 or \
            self.boogle_code.get_path()[-1] in directions \
            and (i,j) not in self.boogle_code.get_path():
            self.boogle_code.set_path((i,j))
            self.buttons[(i, j)]['bg'] = PASS_COLLOR
            st = str(self.boogle_code.get_board_value(i,j))
            self.current_word["text"] += st

    def check_word(self):
        """when button of check word is clicked- method checks if word is in
        defined dict. if so-
        score is updated and word is added to used words label.
        finally, label of written word is cleared and pressed path of
        buttons is released."""
        word = self.boogle_code.get_word()
        if word != '':
            self.used_words["text"] += '{}\n'.format(word)
            score = self.boogle_code.update_score()
            self.score_label["text"]='Score: {}'.format(score)
        for button in self.buttons.keys():
            self.buttons[button]['bg'] = BUTTON_COLOR
        self.boogle_code.set_new_path()
        self.current_word["text"] =''

    def update_time(self):
        """prints current time on game board and ends game when time is over"""
        if self.time == 60*1000:
            self.time_label['bg'] = 'red'
        if self.time == 0:
            self.end_game()
            return
        self.time -= 1000
        self.calculate_time()
        self.root.after(1000, self.update_time)

    def calculate_time(self):
        """defines new time left for game end"""
        time_in_seconds = self.time / 1000
        time_in_minutes = time_in_seconds // 60
        time_in_seconds %= 60
        self.time_label.configure(text="Time Left: \n%02d:%02d" % (time_in_minutes, time_in_seconds))

    def end_game(self):
        """initializes frame with options to start a new game
        or guit the software"""

        self.frame.destroy()
        self.root.geometry("350x350")
        self.gameover = PhotoImage(file="s.png")

        self.photo =tk.Label(image=self.gameover)

        self.photo.grid()
        self.frame = tk.Frame(self.root, bg=COLOR)
        self.frame.grid()
        st='Game over! Your score was {} points.\n ' \
            'Would you like another game?'.format(self.boogle_code.get_score())
        self.message = tk.Label(text= st, width=46, height=4,bg=PASS_COLLOR,font=("Comic Sans MS", 10,'bold'))
        self.message.grid()


        self.exit_game = tk.Button(self.frame, text="QUIT GAME", font=("Comic Sans MS", 15,'bold'),
            height=1,width=10, relief= "solid",bg=BUTTON_COLOR, command=self.root.destroy)
        self.exit_game.grid()
        another_game = tk.Button(self.frame, text="NEW GAME",bg=BUTTON_COLOR,
                                 font=("Comic Sans MS", 15,'bold'), height=1,
                                 width=10, relief= "solid", command=lambda:
            [self.frame.destroy(), self.message.destroy(),self.photo.destroy(),
             self.exit_game.destroy(), self.start_game()])
        another_game.grid()