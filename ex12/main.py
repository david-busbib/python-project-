from tkinter import *
import tkinter as tk
from boogle_Board import Board
from copy import deepcopy


BUTTON_COLOR = "#00ffff"
BUTTON_CLICKED = 'gray'
TIME_TEXT = "Time left: 03:00"
TIME = 3 * 60 * 1000
BACKGROUND_COLOR = 'purple'
COLOR = '#00aead'
WORD = 'word you find'
PASS_COLLOR ='green'


class BoardGUI():
    def __init__(self, root):
        # super().__init__(root)
        self.root = root
        self.root.resizable(False, False)
        self.boogle_code = Board()
        self.buttons = {}

        self.frame = tk.Frame(self.root, bg=COLOR)

        self.sub_frame = tk.Frame(self.frame)
        self.frame.grid()
        self.sub_frame.grid(row=5, column=4)
        self.time = TIME

        self.used_words = tk.Label(self.frame, text="", bg=BACKGROUND_COLOR, width=20, height=8,relief=RIDGE)
        self.score_label = tk.Label(self.frame, text='Score: {}'.format(0), font=('Georgia', 20), bg=BACKGROUND_COLOR,relief=SUNKEN,
                                    width=15, height=2)
        self.time_label = tk.Label(self.frame, text=TIME_TEXT, font=('Georgia', 20), bg=BACKGROUND_COLOR, width=16,
                                   height=2)
        self.current_word = tk.Label(self.frame, text='', bg=BACKGROUND_COLOR, width=11, height=4,relief=RIDGE)
        self.type={}
        self.start_game()


    def start_game(self):
        self.root.geometry("600x500")
        self.root.configure(bg=COLOR)
        self.score_label.grid(row=0, column=0, columnspan=2)
        self.time_label.grid(row=0, column=4, columnspan=8)
        self.buttons_frame()
        self.current_word.grid(row=1, column=0, columnspan=2)
        self.used_words.grid(row=4, column=0, columnspan=4, rowspan=5)

        self.check_word = tk.Button(self.frame, font=("tahoma", 10), command=self.check_word, width=11, height=2,
                                    bg=BACKGROUND_COLOR, text='check word')
        self.check_word.grid(row=3, column=len(self.boogle_code.get_board()[0]) + 1, rowspan=3, columnspan=3)
        self.root.after(1000, self.update_time)

    def buttons_frame(self):
        board = deepcopy(self.boogle_code.get_board())
        for i in range(len(board)):
            for j in range(len(board[0])):
                current_button = tk.Button(self.sub_frame,
                                           text=board[i][j], bg=BUTTON_COLOR, font=("tahoma", 20, "bold"),
                                           height=1, width=3, borderwidth=1, relief="sunken",
                                           command=lambda i=i, j=j: self.checker(i,j))  # lambda is passed parameters i and j
                # Grid occurs on a new line
                current_button.grid(row=i + 3, column=j)
                board[i][j] = current_button
                self.buttons[(i, j)] = current_button
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


    def checker(self, i, j):
        directions = [(i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1),
                      (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1)]
        if len(self.boogle_code.get_path()) == 0 or \
                self.boogle_code.get_path()[-1] in directions \
                and (i, j) not in self.boogle_code.get_path():
            self.boogle_code.set_path((i, j))
            self.buttons[(i, j)]['bg'] = BUTTON_CLICKED
            print('hi', self.boogle_code.get_board())
            st = str(self.boogle_code.get_board_value(i, j))
            self.current_word["text"] += st

    def check_word(self):
        word = self.boogle_code.get_word()
        if word != '':
            self.used_words["text"] += '{}\n'.format(word)
            score = self.boogle_code.update_score()
            self.score_label["text"] = 'Score: {}'.format(score)
        for button in self.buttons.keys():
            self.buttons[button]['bg'] = BUTTON_COLOR
        self.boogle_code.set_new_path()
        self.current_word["text"] = ''

    def update_time(self):
        if self.time == 60 * 1000:
            self.time_label['bg'] = 'red'
        if self.time == 0:
            self.end_game()
        self.time -= 1000
        self.calculate_time()
        self.root.after(1000, self.update_time)

    def calculate_time(self):
        time_in_seconds = self.time / 1000
        time_in_minutes = time_in_seconds // 60
        time_in_seconds %= 60
        self.time_label["text"] = "Time Left: \n%02d:%02d" % (time_in_minutes, time_in_seconds)

    def end_game(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root, bg='green')
        self.frame.grid()
        st = 'Game over! Your score was {} points. ' \
             'Would you like another game?'.format(self.boogle_code.get_score())
        self.message = tk.Label(text=st)
        self.message.grid()
        # need to create 2 buttons