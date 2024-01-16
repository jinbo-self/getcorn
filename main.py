import time

from function import clickImage, findImageLoc

image_path = 'image'
time.sleep(3)


x,y,FLAG = findImageLoc('image'+'/EVENTS.png')
print(FLAG)
if FLAG:
    clickImage(x,y)
