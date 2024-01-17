import cv2
from paddleocr import PaddleOCR,draw_ocr
from function import grab_screen


#输出图片文字
def FindStr(imgPath):
    ocr = PaddleOCR()
    img = imgPath#cv2.imread(imgPath)

    result = ocr.ocr(img, cls=False)
    print(result,1)
    for line in result:
        #print(line,2)
        for line_1 in line:
            print(line_1,3)
            if line_1[-1][0] == "EVENTES":
                return line_1[-1][0]



inputImage = grab_screen(
        x=0,
        x_w=1920,
        y=0,
        y_h=1080)
if FindStr(inputImage)=="EVENTES":
    print("OK!")