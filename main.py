import time

import cv2

from function import clickImage, findImageLoc

#定位游戏方框/大小
cube_left_x, cube_left_y, _ = findImageLoc('cube_left.png')
cube_right_x, cube_right_y, _ = findImageLoc('cube_right.png')

#顶线平行
if cube_left_y < cube_right_y:
    cube_right_y = cube_left_y
else:
    cube_left_y = cube_right_y
cube_w = cube_right_x - cube_left_x
cube_h = cube_w*712/1265
print(cube_left_x,cube_left_y)
print(cube_right_x,cube_right_y)
#边线比例为：1265/712

