#################################################################
# FILE :quadratic_equation
# WRITER : david busbib, dbusbib123 , 336224076
# EXERCISE : intro2cs2 ex1 2022
# DESCRIPTION: A simple program
# NOTES: two fuction that returnt the valua of a calcule operation in math
#################################################################
import math
def quadratic_equation(a,b,c): #
    if b ** 2 - 4 * a * c < 0:  #  if this happen we will get a error
        return None, None
    else:
        # the two sulotion of quadratic problem are
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if b**2 - 4*a*c > 0 :
            return x1 , x2
        elif b**2 - 4*a*c == 0:
             return x1,None

def quadratic_equation_user_input():

    a, b, c = input("Insert coefficients a, b, and c:").split()
    a=float(a) ; b=float(b); c=float(c)
    if a == 0:
        print(" The parameter 'a' may not equal 0")
    else:
        X = quadratic_equation(a,b,c)[0] ; Y = quadratic_equation(a,b,c)[1]
        if X != None and Y != None:#that mean that we have two solotion
            print(' The equation has 2 solutions: {} and {}'.format(X,Y))
        elif X!=None and Y == None :# that maen that we have only one solution
            print(' The equation has 1 solution:',X)
        else:
            print(' The equation has no solutions')


