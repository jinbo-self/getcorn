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


# 边线比例为：1265/712

# 相对于的cube的坐标比例 events_x * cube_w + cube_left_x，events_y * cube_h + cube_left_y
def trans(x_ratio, y_ratio):
    x = x_ratio * cube_w + cube_left_x
    y = y_ratio * cube_h + cube_left_y
    return int(x), int(y)


#events_x, events_y = trans(1.00, 0.47)
EVENTS_x,EVENTS_y = trans(0.97,0.48)
EVENTS_x_w,EVENTS_y_h = trans(1.03,0.51)

STORIES_x, STORIES_y = trans(-0.04, 0.16)
STORIES_x_w, STORIES_y_h = trans(0.08, 0.20)
the_first_stories_x,the_first_stories_y = trans(0.05, 0.38)
add_unicorn_x, add_unicorn_y = trans(0.46, 0.45)


is_first_page = False
is_events_page = False
while True:
    time.sleep(1)
    if cube_left_flag and cube_right_flag \
            and FindStr(grab_screen(EVENTS_x, EVENTS_x_w, EVENTS_y, EVENTS_y_h), path=False) == "EVENTS":
        is_first_page = True
        #clickImage(events_x, events_y)
        clickImage(int((EVENTS_x + EVENTS_x_w) / 2), int((EVENTS_y + EVENTS_y_h) / 2))
        time.sleep(1)
        image = grab_screen(STORIES_x, STORIES_x_w, STORIES_y, STORIES_y_h)
        # cv2.imshow('screen', image)
        # cv2.waitKey(0)
        if FindStr(grab_screen(STORIES_x, STORIES_x_w, STORIES_y, STORIES_y_h), path=False) == "STORIES":
            is_events_page = True
            is_first_page = False
            clickImage(int((STORIES_x + STORIES_x_w)/2),int((STORIES_y+STORIES_y_h)/2))
            time.sleep(1)
            clickImage(the_first_stories_x,the_first_stories_y)
            time.sleep(1)
            clickImage(add_unicorn_x, add_unicorn_y)
            time.sleep(1)


