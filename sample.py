import pytesseract
import cv2
import io 
from PIL import ImageFont, ImageDraw, Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("img3.png")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgh, imgw = grey.shape
img2 = np.zeros((imgh, imgw, 3), np.uint8)

text = pytesseract.image_to_data(img, lang="amh")
imgpil = Image.fromarray(img2)
draw = ImageDraw.Draw(imgpil)
font = ImageFont.truetype(".\AbyssinicaSIL-Regular.ttf", 32)

for x, i in enumerate(text.splitlines()):
            
            if x != 0 and len(i.split()) == 12:
                i = i.split()
                x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)


cv2.imshow("real", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
