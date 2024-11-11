from typing import *
from ex7_helper import *

def mult(x: float, y: int) -> float:
    #get two number one float one int and returnt x*y
    if y==0:
        return 0
    else:
        return  add(x,mult(x,subtract_1(y)))


def is_even(n: int) -> bool:
    if n== 2 :
        return True
    elif n==1 :
        return False
    return is_even(subtract_1(subtract_1(n)))

def log_mult(x: float, y: int) -> float:
    if y== 0:
        return 0
    count = log_mult(x,divide_by_2(y))
    if is_odd(y) == False:
        return add(count,count)
    return add(x,add(count,count))

def reverse(s: str) -> str:
    if len(s) ==0 or len(s) ==1:
        return s
    else:
        return append_to_end(reverse(s[1:]),s[0])

def help8(n:int) -> int :
    if n==0:                          
        return 0                      
    mudulu = n % 10                   
    if mudulu == 1:                   
        return 1 + help8(n //10)      
    return help8(n // 10)             
def number_of_ones(n: int) -> int:
    if n==0:
        return 0
    return help8(n)+ number_of_ones(n-1)

def help_magic(n : int,lst :List[Any],n_lst : List[Any]) -> List[Any]:
    if n==0:
        return lst
    help_magic(n-1,lst,[])
    n_lst = magic_list(n - 1)
    lst.append(n_lst)
    return lst

def magic_list(n:int) -> List[Any]:
    if n==0:
        return []
    lst:List[Any] = []
    n_lst :List[Any]=[]
    return help_magic(n,lst,n_lst)

def is_power(b: int, x: int) -> bool:
    if b == x or x ==1 :
        return True
    if b > x or (b <=1 and x!=1) :
        return False
    return is_power_help(b,x, 1)

def is_power_help( b:int, x :int, n:float) ->bool:
    if n > x:
        return False
    if n == x:
        return True
    return is_power_help(b, x, log_mult(b,n))

def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any) ->Any :
    if n > 0:
        play_hanoi(Hanoi, n - 1, src, temp, dst)
        Hanoi.move(src, dst)
        play_hanoi(Hanoi, n - 1, temp, dst, src)


def compare_2d_lists(l1:List[int], l2:List[int])-> bool:
    if len(l1)!= len(l2):
        return False
    if len(l1) ==0:
        return help_compare(l1,l2)
    else:
        return foo(l1, l2, j=0)

def foo(l1:List[int], l2:List[int],j:int)-> bool:
    if len(l1) == len(l2) == 1:
        return help_compare(l1,l2)
    else:
        b=help_compare(l1[j], l2[j])
        if b:
            if j+1< len(l1):
                return foo(l1, l2, j + 1)
            return b
        else:
            return False

def help_compare(l1:Any, l2:Any)-> bool:
    if l1 or l2:
        if len(l1) != len(l2) or l1[0] != l2[0]:
            return False
        return help_compare(l1[1:],l2[1:])
    else:
        return True


