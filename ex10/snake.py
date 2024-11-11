"""
Names: Yogev Shapira, David Busbib
Usernames: yogev.shapira, dbusbib123
File: snake.py
Students I discussed the exe with: Bezalel Yanir, Oryan Hassidim
Web pages I used:
"""
from game_parameters import WIDTH, HEIGHT, get_random_bomb_data,\
    get_random_apple_data

class Bomb:
    """initializes object of bomb"""
    def __init__(self):
        self.x, self.y, self.radius, self.time = get_random_bomb_data()
        self.small_radius = 0
    def get_bomb_coordinates(self):
        return self.x, self.y, "red"
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_time(self):
        return self.time
    def set_time(self):
        """decreaese the time left till explosion by one"""
        self.time-=1
    def get_waves(self):
        """returns list with all cells who appear in the bomb wave
        at current bomb, if waves are over- return None"""
        if self.small_radius <= self.radius:
            lst = []
            for i in range(WIDTH):
                for j in range(HEIGHT):
                    if abs(self.x - i) + abs(self.y - j) == self.small_radius:
                        lst.append((i,j,"orange"))
            self.small_radius += 1
            return lst
        else:
            self.small_radius += 1
            if self.small_radius == self.radius:
                self.small_radius = 0
            return

class Apple:
    """initializes object of Apple"""
    def __init__(self):
        self.x, self.y, self.score = get_random_apple_data()
    def get_apple_coordinate(self):
        """returns cell that will be added to lst in Board"""
        return self.x, self.y, "green"
    def get_apple_x(self):
        return self.x
    def get_apple_y(self):
        return self.y
    def get_apple_score(self):
        return self.score

class Snake:
    """initializes object of snake"""
    def __init__(self):
        self.coor = [(WIDTH//2, (HEIGHT//2)-2, "black"),
                     (WIDTH//2, (HEIGHT//2)-1, "black"),
                     (WIDTH//2, (HEIGHT//2), "black")]
        # initializes list of tuples representing snake's cell on board
        self.dir = "Up" # first direction where snake is headed
        self.erase_tail = 0
        # represents how many times snake tail should not be removed (happens
        # when apple is eaten
    def set_direction(self, direction):
        """gets new direction to lead snake and sets it
        if direction is legal """
        if direction in ["Right", "Left"] and self.dir in ["Up", "Down"]\
        or direction in ["Up", "Down"] and self.dir in ["Right", "Left"]:
            self.dir = direction
    def set_erase_tail(self):
        """sets 3 turns where snake tail wouldn't be removed"""
        self.erase_tail = 3
    def get_snake_coordinates(self):
        return self.coor

    def move(self):
        """updates new coordinates of snake on game board
        according to its direction"""
        x_head, y_head = self.coor[-1][0], self.coor[-1][1]
        # appends new head to snake coordinates
        if self.dir == 'Up':
            self.coor.append((x_head, y_head+1, "black"))
        if self.dir == 'Down':
            self.coor.append((x_head, y_head-1, "black"))
        if self.dir == 'Right':
            self.coor.append((x_head+1, y_head, "black"))
        if self.dir == 'Left':
            self.coor.append((x_head-1, y_head, "black"))
        if not self.erase_tail > 0: # removes tail from snake if needed
            self.coor.pop(0)
        self.erase_tail -= 1

    def next_move(self):
        """gets next location of snake head on game board
        according to direction"""
        x_head, y_head = self.coor[-1][0], self.coor[-1][1]
        if self.dir == 'Up':
            return (x_head, y_head + 1)
        if self.dir == 'Down':
            return (x_head, y_head - 1)

        if self.dir == 'Right':
            return (x_head + 1, y_head)
        if self.dir == 'Left':
            return (x_head - 1, y_head)
