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
print(cube_left_x, cube_left_y)
print(cube_right_x, cube_right_y)
# 边线比例为：1265/712

# 相对于的cube的坐标比例 events_x * cube_w + cube_left_x，events_y * cube_h + cube_left_y
events_x, events_y = 0, 0

STORIES_x, STORIES_x_w, STORIES_y, STORIES_y_h = 0, 0, 0, 0

is_first_page = False
is_events_page = False
while True:
    time.sleep(1)
    if cube_left_flag and cube_right_flag:
        is_first_page = True
        clickImage(events_x, events_y)
        if FindStr(grab_screen(STORIES_x, STORIES_x_w, STORIES_y, STORIES_y_h)) == "STORIES":
            is_events_page = True
            is_first_page = False

