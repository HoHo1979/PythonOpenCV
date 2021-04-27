import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pytesseract as pt
from pyzbar import pyzbar

p1 = cv2.CascadeClassifier("cascade/haarcascade_frontalface_alt.xml")

p2=cv2.VideoCapture(0)
# print("寬度",p1.get(3))
# print("高度",p1.get(4))
# print("每秒影格數",p1.get(5))
# p1.set(1,6000)

w=int(p2.get(3))
h=int(p2.get(4))

# r1=cv2.VideoWriter("1.mp4", cv2.VideoWriter_fourcc(*'MP4V'),30, (w,h))

while p2.isOpened()==True:
	ret1,m1=p2.read()

	if ret1 == True:
		
		
		ret = p1.detectMultiScale(m1,minNeighbors=1,minSize=(5,5))

		for x,y,w,h in ret:
			cv2.rectangle(m1,(x,y),(x+w,y+h),(0,255,0),2)


		cv2.imshow("Image 1",m1)
		if cv2.waitKey(33)!=-1:
			break
	else:
		break


ret1.release()

