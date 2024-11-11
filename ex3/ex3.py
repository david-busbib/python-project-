def input_list():#we are going to put the num on a lst and their value
 your_input = input()
 lst =[] ; count = 0
 while your_input !='' :
     num = float(your_input)
     lst.append(num)
     count += num
     your_input = input()
 lst.append(count)
 return lst

#q2

def inner_product(vec_1, vec_2):
    #do you know how to calculate to  vec ,if no in this,,,
    # funcion we are going to calculate the value of two vec
    count = 0
    if len(vec_1) != len(vec_2):
        return None
    elif vec_1 == []:
        return count
    else:
        for i in range(len(vec_1)):
            count+= vec_2[i]*vec_1[i]
        return count
#q3
#we gone a use a help to calculate if the lst is one of the four ,
# to check that we will first find what aswer are true and what false
def is_answr1_true(sequence):#we are chaking if answer one is true
    answer1= True
    count = 1
    for i in sequence[1:]:
        if i >= sequence[count - 1]:
            pass
        else:
            answer1 = False
            break
        count += 1
    return answer1
def is_answr2_true(sequence):
    answer2=True#so on we are also chking if answer two is true
    count = 1
    for i in sequence[1:]:
        if i > sequence[count - 1]:
            pass
        elif i <= sequence[count - 1]:
            answer2 = False
            break
        count += 1
    return answer2
def is_answr3_true(sequence):# cheking if answer 3 is true
    answer3 =True
    count = 1
    for i in sequence[1:]:
        if i <= sequence[count - 1]:
            pass
        else:
            answer3 = False
            break
        count += 1
    return answer3
def is_answr4_true(sequence):#cheking if answer four is true
    answer4 = True
    count = 1
    for i in sequence[1:]:
        if i < sequence[count - 1]:
            pass
        else:
            answer4 = False
            break
        count += 1
    return answer4
def sequence_monotonicity(sequence):#with the help of the last four funcion ,
    #we can now know what is the true answer
    lst =[]
    if not sequence:
        return [True,True,True,True]
    else:
        lst.append(is_answr1_true(sequence))
        lst.append(is_answr2_true(sequence))
        lst.append(is_answr3_true(sequence))
        lst.append(is_answr4_true(sequence))
    return lst
#q4
def monotonicity_inverse(def_bool):
    #we want to know what lst are corsponding to the right answer ,
    #so in this fun we gone a discovere how
    lst5 = [1,1,1,1] ; lst1 = [4,3,2,1]
    lst2 = [4,4,3,1] ;  lst3 = [1,1,3,4]
    lst4 = [1,1.5,2,3] ; lst6 = [1,3,0,1]
    if def_bool[0] == def_bool[1]==def_bool[2] == def_bool[3]== False:
        return lst6
    if def_bool[0] == def_bool[1] == def_bool[2] == def_bool[3] :
        return None
    if def_bool[0]:
        if def_bool[1] == True and (def_bool[2] or def_bool[3])==True:
            return# in this case there is no correct lst
        if def_bool[2] and def_bool[3] == False :
            return lst5#in this case the lst num 5 match because its responding to the criter
        if def_bool[3] == True:
            return# in this case there is no correct lst
        if def_bool[1] == False :
            return lst3# here the correcrt lst will be lst 3
        else:
            return lst4
    if def_bool[1] == True :#lets talk about this case
        return #there is no correct lst for that demande
    if def_bool[2] == True:
        if def_bool[3]== True :
            return lst1#now lst1 is the right one
        return lst2
    if def_bool[3] == True:
        return
    return #if nothing coraspon to the criter return Nada
#q5
def is_prime_very_fast(n):#from the lab exs
    if n == 1:
        return False
    if n % 2 == 0 and n != 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
def primes_for_asafi(n):
    #how much prime do you want me to find
    lst=[]
    if n==0:
        return []
    else:
        i = 2
        value =0
        while value < n :
            if is_prime_very_fast(i)==True :
                lst.append(i)
                i+=1; value +=1
            else:
                i+=1
    return lst
#q6
def sum_of_vectors(vec_lst):
    if vec_lst == []:
        return None
    else:
        lst = []
        for i in range(len(vec_lst[0])):
            count = 0
            for j in range(len(vec_lst)):
                count += vec_lst[j][i]
            lst.append(count)
        return lst
#q7
def num_of_orthogonal(vectors):#in this funcion we gone a calcul how much vector arevertical
    count = 0
    for i in range(len(vectors)):
        for j in range(i+1,len(vectors)):
            if inner_product(vectors[i],vectors[j]) == 0:
                count +=1
    return count


