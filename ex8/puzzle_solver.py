from typing import List, Tuple, Set, Optional
from copy import deepcopy


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]

def get_place_col(picture: Picture,row: int, col: int)-> int:
    count =0
    leanth = len(picture[0])
    for i in range(col,leanth):
        if picture[row][i] == 0 :
            break
        count += 1
    j = 1
    while col -j >=0 :
        if picture[row][col-j] == 0:
            break
        count+=1
        j+=1
    return count

def get_place_row(picture:Picture,row: int, col: int)-> int:
    count =0
    leanth = len(picture)
    for i in range(row+1,leanth):
        if picture[i][col] == 0 :
            break
        count += 1
    j = 1
    while (row -j) >= 0 :
        if picture[row-j][col] == 0:
            break
        count+=1
        j+=1
    return count

def max_seen_cells(picture:Picture, row: int, col: int) -> int:
    num = picture[row][col]
    if num == 0:
        return 0
    return get_place_col(picture,row,col) + get_place_row(picture,row,col)

def get_place_col_min(picture: Picture,row: int, col: int)-> int:
    count =0
    leanth = len(picture[0])
    for i in range(col,leanth):
        if picture[row][i] in [0,-1] :
            break
        count += 1
    j = 1
    while col -j >=0 :
        if picture[row][col-j] in [0,-1]:
            break
        count+=1
        j+=1
    return count

def get_place_row_min(picture:Picture,row: int, col: int)-> int:
    count =0
    leanth = len(picture)
    for i in range(row+1,leanth):
        if picture[i][col] in [0,-1] :
            break
        count += 1
    j = 1
    while (row -j) >= 0 :
        if picture[row-j][col] in [0,-1]:
            break
        count+=1
        j+=1
    return count

def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    num = picture[row][col]
    if num  in [0,-1]:
        return 0
    return get_place_col_min(picture, row, col) + get_place_row_min(picture, row, col)

def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    first:int = 0
    second:int = 0
    third:int = 0
    for tpl in constraints_set:
        row = tpl[0]; col = tpl[1]; answer = tpl[2]
        max_a = max_seen_cells(picture,row,col)
        min_a = min_seen_cells(picture,row,col)
        if answer == max_a and answer == min_a:
            first+=1
        elif min_a <= answer <= max_a:
            second +=1
        else:
            third +=1
    if third >0:
        return 0
    if first == len(constraints_set):
        return 1
    return 2

def help_to_solve( constraints_set: Set[Constraint], answer: List,
     n: int, m: int,pic1:List,lst: List) -> None:
    if len(answer) == 1 :
        return
    if n * m < len(lst):
        return
    new_pic = deepcopy(pic1)
    k= 0
    b =0
    while b < n :
        a =0
        while a < m:
            if not k >= len(lst):
                new_pic[b][a] = lst[k]
            k += 1
            a+=1
        b+=1
    check= check_constraints(new_pic, constraints_set)
    if check == 0 :
        return
    if len(lst) == n * m and check == 1:
        answer.append(new_pic)
    help_to_solve(constraints_set, answer, n, m, pic1,lst+[1])
    help_to_solve(constraints_set, answer, n, m, pic1,lst+[0])


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    answer = [] ;  lst = []
    pic1 = [[-1 for i in range(m)] for j in range(n)]
    help_to_solve(constraints_set, answer, n, m, pic1,lst)
    if not len(answer):
        return
    return answer[0]
def help_find_sulotion( constraints_set: Set[Constraint], answer:List,
     n: int, m: int , pic1:List,lst: list) -> None:
    new_pic = deepcopy(pic1)
    if n * m < len(lst):
        return
    k= 0
    b = 0
    while b < n:
        a = 0
        while a < m:
            if not k >= len(lst):
                new_pic[b][a] = lst[k]
            k += 1
            a += 1
        b += 1
    check =check_constraints(new_pic,constraints_set)
    if len(lst) ==  n * m and check == 1:
        answer.append('you pass one ,now another one ')
    if check == 0:
        return
    help_find_sulotion( constraints_set, answer, n, m, pic1,lst + [1])
    help_find_sulotion(constraints_set, answer , n, m,pic1,lst + [0])

def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    answer = [] ; lst = []
    pic1 = [[-1 for i in range(m)] for j in range(n)]
    help_find_sulotion(constraints_set, answer, n, m,pic1,lst)
    new_ans = len(answer)
    return new_ans




def generate_puzzle(picture: Picture) -> Set[Constraint]:
    if picture == [[1]]:
        return {(0,0,1)}
    ...