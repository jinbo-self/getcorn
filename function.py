import ctypes
import time

import cv2
import numpy as np
import win32con
import win32gui
import win32ui


#获取全屏
def grab_screen(x, x_w, y, y_h):
    # 获取桌面
    hwin = win32gui.GetDesktopWindow()

    w = x_w - x
    h = y_h - y

    # 返回句柄窗口的设备环境、覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hwindc = win32gui.GetWindowDC(hwin)

    # 创建设备描述表
    srcdc = win32ui.CreateDCFromHandle(hwindc)

    # 创建一个内存设备描述表
    memdc = srcdc.CreateCompatibleDC()

    # 创建位图对象
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, w, h)
    memdc.SelectObject(bmp)

    # 截图至内存设备描述表
    memdc.BitBlt((0, 0), (w, h), srcdc, (x, y), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    # 内存释放
    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

def findImageLoc(templateImage):
    # 加载训练图A.JPG和待检测图C.JPG
    template = cv2.imread(templateImage)  #模版图像
    inputImage = grab_screen(
        x=0,
        x_w=1920,
        y=0,
        y_h=1080)

    # inputImage  = cv2.cvtColor(inputImageFile, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
    # template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
    # cv2.imshow('screen', inputImage)
    # cv2.waitKey(0)

    # 加载B.JPG并从A.JPG中截取
    res = cv2.matchTemplate(inputImage, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)  # 找到匹配的位置

    for pt in zip(*loc[::-1]):
        print(pt)
        x, y = pt[0], pt[1]
        w, h = template.shape[1], template.shape[0]  # 边界矩形的宽度和高度等于模板的宽度和高度
        cv2.rectangle(inputImage, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 在图像上绘制边界矩形
        return x + w / 2, y + h / 2,True

    return 0,0,False
    # 模拟鼠标点击
# 定义MOUSEINPUT结构体
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

# 定义INPUT结构体
class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("mi", MOUSEINPUT)]

def clickImage(x,y):
    # 定义常量
    INPUT_MOUSE = 0
    MOUSEEVENTF_LEFTDOWN = 0x02
    MOUSEEVENTF_LEFTUP = 0x04
    MOUSEEVENTF_ABSOLUTE = 0x8000

    # 获取屏幕分辨率
    user32 = ctypes.windll.user32


    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # 移动光标
    mouse_x = int(x)  # 将x_value转换为整数类型
    mouse_y = int(y)  # 将y_value转换为整数类型
    user32.SetCursorPos(mouse_x, mouse_y)

    # 将坐标转换为65536比例的绝对坐标
    x = int(x * 65536 / screen_width)
    y = int(y * 65536 / screen_height)

    print(x,y,screen_width,screen_height)

    mouse_input_down = MOUSEINPUT()
    mouse_input_down.dx = x
    mouse_input_down.dy = y
    mouse_input_down.mouseData = 0
    mouse_input_down.dwFlags = MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_ABSOLUTE
    mouse_input_down.time = 0
    mouse_input_down.dwExtraInfo = ctypes.pointer(ctypes.c_ulong(0))

    mouse_input_up = MOUSEINPUT()
    mouse_input_up.dx = x
    mouse_input_up.dy = y
    mouse_input_up.mouseData = 0
    mouse_input_up.dwFlags = MOUSEEVENTF_LEFTUP | MOUSEEVENTF_ABSOLUTE
    mouse_input_up.time = 0
    mouse_input_up.dwExtraInfo = ctypes.pointer(ctypes.c_ulong(0))

    # 初始化INPUT实例
    input_down = INPUT()
    input_down.type = INPUT_MOUSE
    input_down.mi = mouse_input_down

    input_up = INPUT()
    input_up.type = INPUT_MOUSE
    input_up.mi = mouse_input_up

    # 创建INPUT数组
    inputs = (INPUT * 2)(input_down, input_up)

    # 发送鼠标事件
    user32.SendInput(2, ctypes.pointer(inputs), ctypes.sizeof(INPUT))




