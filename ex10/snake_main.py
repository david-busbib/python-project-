"""
Names: Yogev Shapira, David Busbib
Usernames: yogev.shapira,dbusbib123
File: snake_main.py
Students I discussed the exe with: Bezalel Yanir, Oryan Hassidim
Web pages I used:
"""
from game_display import GameDisplay
from board import Board

def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    snake_flag1, snake_flag2, snake_flag3 = True, True, True
    b = Board()
    for cell in b.get_board(): # draws all cells with objects on them
        gd.draw_cell(cell[0], cell[1], cell[2])
    gd.end_round()

    while snake_flag1 and snake_flag2 and snake_flag3:
        key_clicked = gd.get_key_clicked() # gets input of direction
        if key_clicked is not None:
            b.sn.set_direction(key_clicked)
        b.sn.move()
        b.update_snake()
        snake_flag1 = b.get_next_turn()
        snake_flag3 = b.snake_hit_itself()
        snake_flag2 = b.check_waves()
        if not snake_flag1 or not snake_flag3 or not snake_flag2:
            for cell in b.get_board():
                gd.draw_cell(cell[0], cell[1], cell[2])
            gd.end_round()
            break
        b.is_apple_eaten()
        gd.show_score(b.get_score())
        b.is_bomb()
        snake_flag2 = b.check_waves()
        for cell in b.get_board():

            gd.draw_cell(cell[0], cell[1], cell[2])
        gd.end_round()


