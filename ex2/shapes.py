#################################################################
# FILE :shape_area
# WRITER : david busbib, dbusbib123 , 336224076
# EXERCISE : intro2cs2 ex2 2022
# DESCRIPTION: A simple program
# NOTES: a fuction that return the value of the area of the shape
#################################################################
import math
def rectangle_shape(a,b): # the way that we calculate a shape of a rectangle
    area = a* b
    return area
def circle_shape(r): # the way the we calculate the circle area
    circle_S = math.pi*pow(r,2)
    return circle_S
def triangle_shape(a):# a funcion that help you to caculate triangle area
    triangle_S =math.sqrt(3) / 4 * pow(a,2)
    return triangle_S

def shape_area(): # now a funciont that demanding the reader to input the shape and the computer will give him the area
    choose = int(input('Choose shape (1=circle, 2=rectangle, 3=triangle): '))
    if not(1 <= choose <= 3) :
        return None
    else:
        if choose == 1:
            r = float(input())
            return circle_shape(r)
        elif choose == 2:
            a = float(input())
            b = float(input())
            return rectangle_shape(a,b)
        elif choose == 3:
            a = float(input())
            return triangle_shape(a)
