import math
# we are going to write the golden ratio with the help of a funcion
def golden_ratio():
    print((1+math.sqrt(5))/2)

def six_squared():
# a fuction that print 6 sqare 2
    print(6**2)

#a funcion that print a math problem with the help of Pythagorean theorem
def hypotenuse():
    print(math.sqrt((12**2)+(5**2)))
#a funcion that print pi
def pi():
    print(math.pi)

#a fuction that print e
def e():
    print(math.e)

#a fuction that print the area of a sqare from one to ten
def squares_area():
    print(1*1,2*2,3*3,4*4,5*5,6*6,7*7,8*8,9*9,10*10)
if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()