import tkinter as tk
from boggle_board_randomizer import randomize_board
class Board:
    def __init__(self):
        self.board = randomize_board()

        self.words_dict = self.load_words_dict("boggle_dict.txt")
        self.path = []
        self.used_words = []
        self.score = 0

    def get_board(self):
        return self.board
    def get_board_value(self, i, j):
        return self.board[i][j]
    def get_path(self):
        return self.path
    def set_path(self, cell):
        self.path.append(cell)
    def set_new_path(self):
        self.path = []
    def get_score(self):
        return self.score

    def update_score(self):
        n = len(self.path)**2
        self.score += n
        return self.score

    def load_words_dict(self, file_name):
        dir = open(str(file_name))
        words = set(line.strip() for line in dir.readlines())
        dir.close()
        return words



    def is_word_repeated(self, word):
        if word in self.words_dict:
            return True
        return False

    def get_word(self):
        word = ''
        for cell in self.path:
            x,y= cell
            word += str(self.board[x][y])
        if word in self.words_dict and word not in self.used_words:
            self.used_words.append(word)
            return word
        return ''

    def has_no_returns(self, path):
        for i in range(len(path) - 1):
            for j in range(i + 1, len(path)):
                if i == j:
                    return False
        return True

    def in_range(self,path):
        """checks if all paths in path are legal
         according to their previous path"""
        for i in range(len(path) - 1):
            x, y = path[i][0], path[i][1]
            next_x, next_y = path[i + 1][0], path[i + 1][1]
            if not len(self.board) >= next_x >= 0 or not len(
                    self.board[0]) >= next_y >= 0:
                return False
            if (next_x, next_y) not in [(x, y + 1), (x + 1, y), (x - 1, y),
                                        (x, y - 1),
                                        (x + 1, y + 1), (x - 1, y - 1),
                                        (x + 1, y - 1), (x - 1, y + 1)]:
                return False
        return True

    def is_valid_path(self, path, words):
        if not self.has_no_returns(path) or not self.in_range(path):
            return
        st = ''
        for tup in path:
            x, y = tup[0], tup[1]
            if len(self.board) - 1 >= x >= 0 and len(self.board[0]) - 1 >= y >= 0:
                st += self.board[x][y]
        if st in words:
            return st
        return




