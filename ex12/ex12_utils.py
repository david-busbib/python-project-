def has_no_returns(path):
    for i in range(len(path)-1):
        for j in range(i+1, len(path)):
            if i == j:
                return False
    return True

def in_range(board, path):
    """checks if all paths in path are legal
     according to their previous path"""
    for i in range(len(path)-1):
        x, y = path[i][0],path[i][1]
        next_x, next_y = path[i+1][0],path[i+1][1]
        if not len(board) >= next_x >= 0 or not len(board[0]) >= next_y >= 0:
            return False
        if (next_x, next_y) not in [(x,y+1),  (x+1,y),  (x-1,y),  (x,y-1),
                                    (x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]:
            return False
    return True

def is_valid_path(board, path, words):
    if not has_no_returns(path) or not in_range(board, path):
        return
    st=''
    for tup in path:
        x, y = tup[0],tup[1]
        if len(board)-1 >= x >= 0 and len(board[0])-1 >= y >= 0:
            st += board[x][y]
    if st in words:
        return st
    return

def helper(n, board, words, st, lst, x, y,flag):
    if n == 0:
        if st in words and flag:
            return lst
        return
    st += board[x][y]
    lst.append((x,y))
    directions =[(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1),
     (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
    for dir in directions:
        if dir not in lst  and len(board)-1 >= dir[0] >= 0 \
                    and len(board[0])-1 >= dir[1] >= 0:
            #print(board,dir)
            # lst.append(dir)
            # st += board[dir[0]][dir[1]]
            return helper(n-1, board, words, st, lst, dir[0], dir[1],flag)

def path_helper(n, board, words, all_paths, x, y):
    if x == len(board):
        return all_paths
    lst = helper(n, board, words, '', [], x, y,True)
    if lst is not None:
        all_paths.append(lst)
    if y == len(board[0])-1:
        return path_helper(n, board, words,all_paths, x+1, 0)
    else:
        return path_helper(n, board, words, all_paths, x, y+1)

def find_length_n_paths(n, board, words):
    all_paths = []
    return path_helper(n, board, words, all_paths, 0, 0)




def find_word(board, word, get_word, lst, all_paths, x, y, index):
    if get_word == word:
        all_paths.append(lst)

    if index >= len(word):
        return all_paths

    directions = [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1),
                  (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1),
                  (x - 1, y + 1)]
    for dir in directions:
        if dir not in lst and len(board) - 1 >= dir[0] >= 0 \
        and len(board[0]) - 1 >= dir[1] >= 0 and \
        (word[index] == board[dir[0]][dir[1]] or (index+len(board[x][y])<=len(word) and
        board[dir[0]][dir[1]] == word[index:index+len(board[x][y])])):
            # lst.append(dir)
            # get_word += board[dir[0]][dir[1]]
            all_paths = find_word(board, word, get_word+ board[dir[0]][dir[1]],
            lst + [dir],all_paths, dir[0], dir[1], index+len(board[dir[0]][dir[1]]))
            # lst.pop()
    return all_paths


def word_helper(board, word, get_word, index):
    lst2=[]
    for x in range(len(board)):
        for y in range(len(board[0])):
            if word[index] == board[x][y]:
                    #or board[x][y] == word[index:index+len(board[x][y])]:
                lst2.extend(find_word(board, word, get_word + board[x][y], [(x,y)], [], x, y, index+len(board[x][y])))
    return lst2



def find_length_n_words(n, board, words):
    words_lst = []
    for word in words:
        if len(word) == n:
            lst=word_helper(board, word,'', 0)
            if lst is not None:
                words_lst.extend(lst)
    return words_lst

def max_score_paths(board, words):
    all_paths = []
    for word in words:
        lst = find_length_n_words(len(word), board, [word])
        max_lst = lst
        max_path = 0
        if len(lst) > 0:
            if isinstance(lst[0], list):
                for path in lst:
                    if len(path) > max_path:
                        max_path = len(path)
                        max_lst = path
            all_paths.append(max_lst)
    return all_paths


board = [
         ['T', 'O', 'B', 'Q']
        ]
word_dict = {'BOT': True}
expected_1 = [[(1, 0), (1, 1), (1, 2)]]
expected_2 = [[(1, 2), (1, 1), (1, 0)]]
print(find_length_n_paths(3, board, word_dict))
"""assert sorted(actual) == sorted(expected_1 + expected_2)"""