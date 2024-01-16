import cv2
from paddleocr import PaddleOCR,draw_ocr
ocr = PaddleOCR()
img = cv2.imread("B.png")

result = ocr.ocr(img,cls=False)

for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)