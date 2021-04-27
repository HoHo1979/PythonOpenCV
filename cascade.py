import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pytesseract as pt
from pyzbar import pyzbar


p1 = cv2.CascadeClassifier("cascade/cascade.xml")

m1 = cv2.imread("Image.jpg",1)

ret = p1.detectMultiScale(m1,minNeighbors=1,minSize=(5,5))

for x,y,w,h in ret:
	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Image 1",m1)
cv2.waitKey(0)

cv2.destroyAllWindows()
