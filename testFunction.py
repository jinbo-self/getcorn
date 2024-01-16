import cv2
from paddleocr import PaddleOCR,draw_ocr
import requests
from bs4 import BeautifulSoup
#输出图片文字
def FindStr(imgPath):
    ocr = PaddleOCR()
    img = cv2.imread("CONNECT.png")

    result = ocr.ocr(img, cls=False)

    for line in result:
        for i in line:
            return i[-1][0]

url = "https://game.cryptounicorns.fun"
print(url)
response = requests.get(url)
if response.status_code==200:
    pass
else:
    print("请求错误")

html = response.content
soup = BeautifulSoup(html,'html.parser')
element = soup.find('div',{'class':'sc-imWYAI iZlvRU'})
print(element)