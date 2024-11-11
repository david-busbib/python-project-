#################################################################
# FILE :is_vormir_safe
# WRITER : david busbib, dbusbib123 , 336224076
# EXERCISE : intro2cs2 ex2 2022
# DESCRIPTION: A simple program
# NOTES:is_vormir_safe we gone a find out
#################################################################
def is_vormir_safe(max_t,day1,day2,day3):
    count = 0# we gone a count in how much day the temperature was high from the max temp
    if day3 > max_t:
        count +=1
    if day2 > max_t:
        count +=1
    if day1 > max_t :
        count += 1
    if count >= 2 :
        return True
    else:
        return  False
    #max_t is the max temperature in the planete vormir



