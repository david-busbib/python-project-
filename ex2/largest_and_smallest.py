#################################################################
# FILE :largest_and_smallest
# WRITER : david busbib, dbusbib123 , 336224076
# EXERCISE : intro2cs2 ex2 2022
# DESCRIPTION: A simple program
# NOTES: two fuction that returnt the biggest value and the lawer
#################################################################
def largest_and_smallest(num1,num2,num3):
    max = num1 ; min =num3  # i prefer to start with this case ,not obligated but its more readeble
    if num1 >= num2 and num1 >= num3 :
        if num2 >= num3:
             return max , min
        else:# if this not happen he will return that case
            min = num2
            return max, min
    elif num2 >= num1 and num2 >= num3:
        max = num2
        if num1 >= num3:
            return max,min
        else:
            min =num1
            return max, min
    elif num3 >= num1 and num3 >= num2:
        max =num3
        if num1 >= num2:
            min = num2
            return max,min
        else:
            min = num1
            return max,min

def check_largest_and_smallest():#we gone a tray all this case and anathere case that i choose becuase its a extreme case
    count=0
    new1, new2 = largest_and_smallest(17,1,6)
    if new1 != 17 and new2 != 1 :
        count +=1
    new1, new2 = largest_and_smallest(1,17,6)
    if new1 != 17 and new2 != 1:
        count +=1
    new1, new2 = largest_and_smallest(1,1,2)
    if new1 != 2 and new2 != 1:
        count += 1
    new1, new2 = largest_and_smallest(12,12,12)
    if new1 != 12 and new2 != 12:
        count += 1
    new1, new2 = largest_and_smallest(-100, 1,100.1)
    if new1 != 100.1 and new2 != -100 :
        count += 1
    if count == 0:
        return True
    else:
        return False
