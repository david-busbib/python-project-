
# FILE: cartoonify.py
# WRITERS:
# EXERCISE: Intro2cs2 ex6 2021-2022
# DESCRIPTION:
##############################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
import copy

from ex6_helper import *
from typing import Optional
import time
import math
import sys

def separate_channels(image):
    new_lst= []
    for v in range(len(image[0][0])):
        lst_n =[]
        for i in range(len(image)):
            lst = []
            for j in range(len(image[0])):
                lst.append(image[i][j][v])
            lst_n.append(lst)
        new_lst.append(lst_n)
    return new_lst


def combine_channels(channels) :
    lst_n = []
    new_lst = []
    copy_channels = channels
    for j in range(len(copy_channels[0])):
        lst_n =[]
        for i in range(len(copy_channels[0][0])):
            lst = []
            for t in range(len(copy_channels)):
                lst.append(copy_channels[t][j][i])
            lst_n.append(lst)
        new_lst.append(lst_n)
    return new_lst
def RGB2grayscale(colored_image):
    length_list = len(colored_image[0])
    new_lst = []
    for j in range(len(colored_image)):
        lst = []
        for i in range(length_list):
            try:
                red = colored_image[j][i][0] ; green = colored_image[j][i][1]; blue = colored_image[j][i][2]
                avarege = round(red*0.299 + green*0.587 + blue * 0.114)
                lst.append(avarege)
            except:
                pass
        new_lst.append(lst)
    return new_lst
def blur_kernel(size):
    lst=[]
    i= 0
    while i < size:
        lst.append(1/(size**2))
        i += 1
    return [lst] * size
def midle(lst):
    #how to find the location of the midle index of the krenel
    mid = len(lst)/2
    return int(mid)
def apply_kernel(image,kernel):
    new_lst = []
    row_num = 0
    for row in image:
        colom_num = 0
        lst = []
        for num in row:
            lst.append(new_krenel(image,kernel,num,row_num,colom_num))
            colom_num += 1
        row_num += 1
        new_lst.append(lst)
    return new_lst
def new_krenel(image,kernel,index,row_num,colom_num):
    mid = midle(kernel)
    count = 0
    print(row_num,colom_num,index)
    J =0
    for j in (range(-mid,mid+1)):
        I =0
        for  i in (range(-mid,mid+1)):
            if colom_num + i < 0 or row_num + j < 0 :
                count += index *kernel[J][I]
            else:
                try:
                    count += image[row_num + j][colom_num + i] * kernel[J][I]
                except:
                    count += index * kernel[J][I]
            I+=1
        J+=1

    if count < 0 :
        return 0
    if count > 255:
        return 255
    return round(count)

def chek(x,y,image):
    x1 = math.floor(x)
    y1 = math.floor(y)
    x2= math.ceil(x)
    y2=math.ceil(y)
    length = len(image[0]) - 1
    if not y2 <=  length :
        y2 = y1
        y1 = math.floor(y1)
    if not x2 <= length :
        x2 = x1
        x1 = math.floor(x1)
    return x1, x2, y1, y2

def bilinear_interpolation(image, y, x):
    x1, x2, y1, y2 = chek(x, y, image)
    a = image[y1][x1]
    b = image[y2][x1]
    c = image[y1][x2]
    d = image[y2][x2]
    delta_x = x-x1
    delta_y = y-y1
    sum = a * (1 - delta_x ) * (1 - delta_y)+b * delta_y * (1-delta_x)+c * delta_x * (1-delta_y) +\
          d * delta_x * delta_y
    return round(sum)
def resize(image, new_height, new_width):
    new_lst = []
    height_old = len(image)
    width_old = len(image[0])
    for r in range(new_height):
        lst = []
        y = (r) * (height_old - 1) * (new_height - 1) ** (-1)
        for c in range(new_width):
            x= (c) * (width_old -1)*(new_width -1)**(-1)
            new_qaurdinate = bilinear_interpolation(image,y,x)
            lst.append(new_qaurdinate)
        new_lst.append(lst)
    return new_lst
def scale_down_colored_image(image, max_size):
    length_width = len(image[0])
    length_higth = len(image)
    sep = separate_channels(image)
    if max_size >= length_higth and max_size >= length_width:
        return
    else:
        if length_width >= length_higth:
            x = max_size
            y = int(length_higth * max_size *(length_width)**(-1))
        else:
            x = int(length_width* max_size * (length_higth)**(-1))
            y= max_size
    for i, chanel_place in enumerate(sep):
         sep[i] = resize(chanel_place, y, x)

    return combine_channels(sep)
def rotate_90(image, direction):
    if direction == 'L':
        line = image
        for row in line:
            row[:] = row[::-1]
        return get_row(line)
    if direction == 'R':
        nlst = get_row(image)
        for row in nlst:
            row[:] = row[::-1]
        return nlst
def get_row(image):
    line = image
    nlst = []
    for i in range(len(line[0])):
        lst = []
        for j in range(len(line)):
            lst.append(line[j][i])
        nlst.append(lst)
    return nlst
def get_edges(image, blur_size, block_size, c):
    copy_image = image
    apply_image = apply_kernel(copy_image, blur_kernel(blur_size))
    r = block_size // 2
    corner = []
    for i in range(len(apply_image)):
        lst =[]
        for j in range(len(apply_image[0])):
            treshold=get_place(apply_image,i,j,r) - c
            if treshold < copy_image[i][j]:
                lst.append(255)
            else:
                lst.append(0)
        corner.append(lst)
    return corner
def get_place(image,x,y,r):
    count = 0
    avarge = 0
    num = image[x][y]
    for i in range(x-r,x+r+1):
        for j in range(y-r, y+r+1):

            if i < 0 or j < 0 :

                count += num
            else:
                try:
                    print(i, j, 7)

                    count += image[i][j]
                except:
                    count += num
            avarge+=1
    print(count/avarge)
    return count/avarge

print(get_edges([[200, 50, 200]], 3, 3, 10))
def quantize(image,N):
    copy_image = copy.deepcopy(image)
    colom = len(image[0])
    row = len(image)
    for y in range(row):
        for x in range(colom):
            floor_num = math.floor(copy_image[y][x] * N / 256 )
            copy_image[y][x] = round((floor_num * (255)) /(N-1))
    return copy_image


def quantize_colored_image(image, N):
        copy_image = copy.deepcopy(image)
        two_dim_image = separate_channels(copy_image)
        i =0
        while i < len(copy_image[0][0]):
            two_dim_image[i] = quantize(two_dim_image[i],N)
            i+=1
        new_3_dim_image = combine_channels(two_dim_image)
        return new_3_dim_image
def add_mask(image1,image2,mask):
    copy_image1= image1
    copy_image2 = image2
    try:
        new_img1 = separate_channels(copy_image1)
        new_img2 = separate_channels(copy_image2)
        lst =[]
        for i in range(len(copy_image1[0][0])):
            lst.append(help_mask(new_img1[i],new_img2[i],mask))
        return combine_channels(lst)
    except:
        return help_mask(copy_image1,copy_image2,mask)
def help_mask(copy_image1,copy_image2,mask):
    row = len(copy_image1)
    colom =len(copy_image2[0])
    new_image = []
    for i in  range(row):
        lst = []
        for j in range(colom):
            first = copy_image1[i][j] * mask[i][j]
            second = copy_image2[i][j] * (1- mask[i][j])
            lst.append(round(first + second))
        new_image.append(lst)
    return new_image
def help_2(get_image):
    for i in range(len(get_image)):
        for j in range(len(get_image[0])):
            get_image[i][j] = get_image[i][j] / 255
    return get_image
def help_1(image,RGB_image,new_gett):
    leanth =len(image)
    for i in range(leanth):
        image[i] = add_mask(image[i],RGB_image,new_gett)
    return image
def cartoonify(image, blur_size, th_block_size, th_c, quant_num_shades):
    new_image = RGB2grayscale(image)
    new_limit = get_edges(new_image,blur_size,th_block_size,th_c)
    mask = help_2(new_limit)
    quan = quantize_colored_image(image,quant_num_shades)
    sep_quan =separate_channels(quan)
    Image = help_1(sep_quan,new_limit,mask)
    return combine_channels(Image)
def help_1(image,RGB_image,new_gett):
    leanth =len(image)
    for i in range(leanth):
        image[i] = add_mask(image[i],RGB_image,new_gett)
    return image
def help_2(get_image):
    for i in range(len(get_image)):
        for j in range(len(get_image[0])):
            get_image[i][j] = get_image[i][j] / 255
    return get_image
