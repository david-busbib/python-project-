#################################################################
# FILE : hello_turtle.py
# WRITER : david busbib, dbusbib123 , 336224076
# EXERCISE : intro2cs2 ex1 2022
# DESCRIPTION: A simple program that drow a bed of flower
# NOTES: ...
#################################################################
import turtle

'''we are going to draw a petal with the help of turtle'''
def draw_petal():
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

def draw_flower():
    # how to drow a flower with thr help of fetal
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

def draw_flower_and_advance():
    # we are going to drow a flower and also advance
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

def draw_flower_bed():
    #how to drow a bed of flower
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

if __name__ == "__main__" :
   draw_flower_bed()
   turtle.done()



