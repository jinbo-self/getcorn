import time

import cv2

from function import clickImage, findImageLoc, grab_screen, FindStr

# 定位游戏方框/大小
cube_left_x, cube_left_y, cube_left_flag = findImageLoc('cube_left.png')
cube_right_x, cube_right_y, cube_right_flag = findImageLoc('cube_right.png')

# 顶线平行
if cube_left_y < cube_right_y:
    cube_right_y = cube_left_y
else:
    cube_left_y = cube_right_y
cube_w = cube_right_x - cube_left_x
cube_h = cube_w * 712 / 1265
print(cube_left_x, cube_left_y,1)
print(cube_right_x, cube_right_y,2)
print(cube_w, cube_h,3)


def res(x, y):
    x = (x - cube_left_x) / cube_w
    y = (y - cube_left_y) / cube_h
    return x, y


x, y = res(1554, 582)
print("比例：", x, y)


def trans(x, y):
    x = x * cube_w + cube_left_x
    y = y * cube_h + cube_left_y
    return x, y


x, y = trans(x, y)
print("还原：", x, y)
