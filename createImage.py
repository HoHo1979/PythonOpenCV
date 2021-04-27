import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# m1 = cv2.imread("paperwork.png",1)
m1 = cv2.imread("lafite.jpg",0)
# w=600
# h=int((w/m1.shape[1])*m1.shape[0])

m2 = m1.copy()

# th,m2[:,:,0] = cv2.threshold(m1[:,:,0],127,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th,m2[:,:,1] = cv2.threshold(m1[:,:,1],127,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th,m2[:,:,2] = cv2.threshold(m1[:,:,2],127,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)

m2 = cv2.adaptiveThreshold(m1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,0)

# m2 = cv2.warpAffine(m1,cv2.getRotationMatrix2D((50,50),45,0.5),(w,h))
# m2= cv2.flip(m1,-1)
# m2 = cv2.resize(m1,(w,h))
# m2 = np.full(m1.shape,(70,70,70),np.uint8)

# m3 = cv2.add(m1,m2)
# m3 = cv2.absdiff(m1,(70,70,70,255))


# cv2.line(m1, (30,10), (280,10), (0,255,0), 2)
# cv2.rectangle(m1, (30,50), (280,100), (0,255,0), 1)
# cv2.circle(m1, (200,200), 50, (50,30,100), -1)

# m1=Image.fromarray(m1)

# ImageDraw.Draw(m1).text((30,30),"咬寫的",(255,0,0),ImageFont.truetype("msjh.ttc",30))

# m1=np.array(m1)

# print(m1)
# m1[150:300,150:300] = m2[200:350,200:350]

cv2.imshow("Image 1",m1)
cv2.imshow("Image 2",m2)
# cv2.imshow("Image 3",m3)


cv2.waitKey()

cv2.destroyAllWindows()

