import pytesseract
import cv2
import io 
from PIL import ImageFont, ImageDraw, Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("img5.jpeg", 0)
# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(grey,0,200,cv2.THRESH_TRIANGLE | cv2.THRESH_BINARY_INV)
img = cv2.medianBlur(img, 5)

th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 2)

# thresh = cv2.merge((thresh,thresh,thresh))
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
# dilation = cv2.dilate(thresh, rect_kernel, iterations=1)

# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# img2 = img.copy()

# for cnt in contours:

#     x,y,w,h = cv2.boundingRect(cnt)

#     rect = cv2.rectangle(img2, (x,y), (x+w, y+h), (0,0,255), 2)

# imgh, imgw = grey.shape
# img2 = np.zeros((imgh, imgw, 3), np.uint8)

# text = pytesseract.image_to_data(img, lang="amh")
# imgpil = Image.fromarray(img2)
# draw = ImageDraw.Draw(imgpil)
# font = ImageFont.truetype(".\AbyssinicaSIL-Regular.ttf", 32)

# for x, i in enumerate(text.splitlines()):
            
#             if x != 0 and len(i.split()) == 12:
#                 i = i.split()
#                 x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
#                 cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)


# cv2.imshow("diletion", dilation)
# cv2.imshow("img", img2)
cv2.imshow("thresh", th)

cv2.waitKey(0)
cv2.destroyAllWindows()
