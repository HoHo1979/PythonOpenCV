import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pytesseract as pt
from pyzbar import pyzbar

m1=  cv2.imread("taiwan.png",1)


ret=pyzbar.decode(m1)

for i in ret:
	print("類型",i.type)
	try:
		print("內容",i.data.decode("utf-8").encode("sjis").decode("utf-8"))
	except:
		print("內容",i.data.decode("utf-8"))
	print("位置",i.rect)
	x,y,w,h=i.rect
	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)


cv2.imshow("Image 1",m1)
cv2.waitKey(0)

cv2.destroyAllWindows()
