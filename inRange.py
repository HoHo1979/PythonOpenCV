import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pytesseract as pt

m1 = cv2.imread("lafite.jpg",1)
# m1 = cv2.imread("paperwork.png",1)
m2 = m1.copy()
m3 = m1.copy()

m2 = cv2.inRange(m1,(56,62,69),(70,80,130))
# m2 = cv2.inRange(m1,(90,190,13),(255,255,255))
# m2 = cv2.absdiff(m2,(255))
m2 = cv2.dilate(m2,np.ones((10,50)))

a,b = cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(b)

cv2.drawContours(m3,a,-1,(0,0,255),2)

for i in range(0,len(a)):
	x,y,w,h = cv2.boundingRect(a[i])
	m4 = m1[y:y+h,x:x+w]
	nw=200
	nh=int(nw/m4.shape[1]*m4.shape[0])
	m4=cv2.resize(m4,(nw,nh))
	cv2.imshow("Image 4"+str(i),m4)
	text = pt.image_to_string(m4,"fra","")
	print(text)
	cv2.rectangle(m1[y:y+h,x:x+w],(x,y),(x+w,y+h),(0,0,255),2)


cv2.imshow("Image 1",m1)
cv2.imshow("Image 2",m2)
cv2.imshow("Image 3",m3)
cv2.imshow("Image 4",m4)
# 
# text = pt.image_to_string(m4,"fra","")

# print(text)

cv2.waitKey()

cv2.destroyAllWindows()