import sys
import os
def read_wordlist(filename):
    #this fuc get a file and read the file
    #and return you a list of all the word that exist in this file
    word_lst =[]
    with open(filename) as f:
        for line in f:
            x = line[:-1]
            word_lst.append(x)
    return word_lst

def read_matrix(filename):
    #this fuc get a matrix and return to the user list of list with all the letter
    matrix =[]
    with open(filename) as file:
        for line in file:
            letter_line = line[:-1].split(',')
            matrix.append(letter_line)
    return matrix
def inverse_matrix(matrix):
        line = matrix
        for row in line:
            row[:]=row[::-1]
        return line
def trampose_matrix(matrix):
    line =matrix
    nlst = []
    try:
        leanght=len(line[0])
    except:
        leanght = 0
    for i in range(leanght):
        lst = []
        for j in range(len(line)):
            lst.append(line[j][i])
        nlst.append(lst)
    return nlst
def inverse_trampose(matrix):
    line=trampose_matrix(matrix)
    for row in line:
        row[:] = row[::-1]
    return line
def diagonal_up_down(matrix,direction):
    try:
        leant_col = len(matrix[0])
    except:
        leant_col=0
    leath_row = len(matrix)
    diag = [[] for _ in range(leath_row + leant_col - 1)]
    if str(direction)=='w':
        for i in range(leant_col):
            for j in range(leath_row):
                diag[i+j].append(matrix[j][i])
        return diag
    if str(direction) =='y':
        diag_min = 1 - leath_row
        for i in range(leant_col):
            for j in range(leath_row):
                diag[-diag_min+i-j ].append(matrix[j][i])
        return diag
def diagonal_inverse(matrix,direction):
    if str(direction)=='x':
        line = diagonal_up_down(matrix,'y')
        for row in line:
            row[:] = row[::-1]
        return line
    if str(direction)=='z':
        line =  diagonal_up_down(matrix,'w')
        for row in line:
            row[:] = row[::-1]
        return line
def word_to_lst(word):
    LEN=len(word)
    letter_str=[word[x] for x in range(LEN) ]
    return letter_str
def letter_to_str(wrd):
    word =''
    for y in wrd:
        word +=y
    return word
def dirction_right(word_list,matrix,lst):

    matrix_line =matrix
    for line in matrix_line:
        for word in word_list:
            for i in range(len(line)):
                if len(word) > len(line[i:]):
                    break
                else:
                    word_l =letter_to_str(line[i:i+len(word)])
                    if word_l == word:
                        lst.append(word)
    return lst
def direction_left(word_list,matrix,lst):
    for line in inverse_matrix(matrix):
        for word in word_list:
            for i in range(len(line)):
                if len(word) > len(line[i:]):
                    break
                else:
                    word_l =letter_to_str(line[i:i+len(word)])
                    if word_l == word:
                        lst.append(word)
    return lst
def direction_down(word_list,matrix,lst):
    matrix_line = trampose_matrix(matrix)
    for line in matrix_line:
        for word in word_list:
            for i in range(len(line)):
                if len(word) > len(line[i:]):
                    break
                else:
                    word_l =letter_to_str(line[i:i+len(word)])
                    if word_l == word:
                        lst.append(word)
    return lst
def direction_up(word_list,matrix,lst):

    matrix_line = inverse_trampose(matrix)
    for line in matrix_line:
        for word in word_list:
            for i in range(len(line)):
                if len(word) > len(line[i:]):
                    break
                else:
                    word_l =letter_to_str(line[i:i+len(word)])
                    if word_l == word:
                        lst.append(word)
    return lst
def diagonal_up_down(matrix,direction):
    try:
        leant_col = len(matrix[0])
    except:
        leant_col=0
    leath_row = len(matrix)
    diag = [[] for _ in range(leath_row + leant_col - 1)]
    if str(direction)=='w':
        for i in range(leant_col):
            for j in range(leath_row):
                diag[i+j].append(matrix[j][i])
        return diag
    if str(direction) =='y':
        diag_min = 1 - leath_row
        for i in range(leant_col):
            for j in range(leath_row):
                diag[-diag_min+i-j ].append(matrix[j][i])
        return diag

def diagonal_inverse(matrix,direction):
    if str(direction) == 'x':
        line = diagonal_up_down(matrix, 'y')
        for row in line:
            row[:] = row[::-1]
        return line
    if str(direction)=='z':
        line =  diagonal_up_down(matrix,'w')
        for row in line:
            row[:] = row[::-1]
        return line
def dirction_diag(word_list,matrix,direcion,lst):
    matrix_line = diagonal_up_down(matrix,direcion)
    for line in matrix_line:
        for word in word_list:
            for i in range(len(line)):
                if len(word) > len(line[i:]):
                    break
                else:
                    word_l =letter_to_str(line[i:i+len(word)])
                    if word_l == word:
                        lst.append(word)
    return lst

def dirction_inverse_diag(word_list,matrix,direcion,lst):
    matrix_line = diagonal_inverse(matrix,direcion)
    for line in matrix_line:
        for word in word_list:
            for i in range(len(line)):
                if len(word) > len(line[i:]):
                    break
                else:
                    word_l =letter_to_str(line[i:i+len(word)])
                    if word_l == word:
                        lst.append(word)
    return lst
def count_word(lst):
    the_lst = []
    while lst != []:
        word = lst[0]
        count = lst.count(word)
        while word in lst:
                lst.remove(word)
        the_lst.append((word, count))
    return the_lst
def find_words(words_list,matrix,direction):
    lst_result = []
    if 'u' in direction:
        lst_result = direction_up(words_list,matrix, lst_result)
    if 'd'in direction:
        lst_result = direction_down(words_list, matrix, lst_result)
    if 'r' in direction:
        lst_result = dirction_right(words_list, matrix,lst_result)
    if 'l' in direction:
        lst_result = direction_left(words_list, matrix, lst_result)
        (matrix)
    if 'w' in direction:
        lst_result = dirction_diag(words_list, matrix , 'w' , lst_result)
    if 'y' in direction:
        lst_result = dirction_diag(words_list, matrix, 'y', lst_result)
    if 'x' in direction:
        lst_result = dirction_inverse_diag(words_list, matrix, 'x', lst_result)
    if 'z' in direction:
        lst_result = dirction_inverse_diag(words_list, matrix,'z', lst_result)
    return count_word(lst_result)
def write_output(result,filename):
    with open(filename,'w') as f:
        for tup in result:
            f.write(tup[0] + ',' + str(tup[1]) + '\n')
DIRECTION=['x','y','w','l','r','d','u']

def check_input_args(parameters):
    if len(parameters) != 5:
        return 'wrong files please enter corrert file unless you want to mess with my program'
    if not os.path.isfile(parameters[2]) or not os.path.isfile(parameters[1]) :
        return 'wrong files please enter corrert file unless you want to mess with my program'
    for i in parameters[4]:
        if i not in DIRECTION:
            return 'wrong files please enter corrert file unless you want to mess with my program'
def main(parameters):
    validaion = check_input_args(parameters)
    if validaion == None:
        word_file = sys.argv[1]
        Matrix_file = sys.argv[2]
        opt_file = sys.argv[3]
        direction_file = sys.argv[4]
        words=read_wordlist(word_file)
        matrix=read_matrix(Matrix_file)
        dirctions=direction_file
        the_result=find_words(words,matrix,dirctions)
        write_output(the_result,opt_file)
    else:
        print(validaion)

if __name__ == '__main__':
    main(sys.argv)

main (kvkjnkv)