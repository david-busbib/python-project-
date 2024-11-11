from typing import List, Tuple, Set, Optional


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
    first = 0
    second = 0
    third = 0
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

def pic(lst, n, m):
    pic1 = [[-1 for i in range(m)]for j in range(n)]
    k = 0
    for b in range(n):
        for a in range(m):
            if k < len(lst):
                pic1[b][a] = lst[k]
            k += 1
    return pic1

def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture ]:
    pass
def helper():
    ...
def nen_image(n,m,):
    pass
