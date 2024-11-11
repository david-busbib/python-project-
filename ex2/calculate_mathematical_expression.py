#################################################################
# FILE :calculate_mathematical_expression
# WRITER : david busbib, dbusbib123 , 336224076
# EXERCISE : intro2cs2 ex2 2022
# DESCRIPTION: A simple program
# NOTES: two fuction that returnt the valua of a calcule operation in math
#################################################################
def calculate_mathematical_expression(num1,num2,calcul):
    if calcul=='+':      # if the calcul is + please do that
        return num1 + num2
    elif calcul=='-':
        return num1 - num2
    elif calcul == '*':
        return num1 * num2
    elif calcul== ':':
        if num2 == 0 :       #we use that if because we cant divide a num in zero
            return None
        else:
            return num1 / num2
    else:#if you choose to put a str that is not in the list you wil get None
        return None
#q2
def calculate_from_string(z):#z = a string with two number and one calcul opeator a string with  5 place
    lst_expression = z.split()# z is a string of 5 place for example we can say {1,'+',2,sep=' '}
    calcul1 = lst_expression[1]
    num_1 =float(lst_expression[0])
    num_2 = float(lst_expression[2])
    return calculate_mathematical_expression(num_1,num_2,calcul1)

