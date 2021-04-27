import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

m1 = cv2.imread("lafite.jpg",1)
m2 = m1.copy()
m3 = m1.copy()

m3=cv2.dilate(m1,np.ones((1,5)))
m2=cv2.erode(m3,np.ones((1,5)))

cv2.imshow("Image 1",m1)
cv2.imshow("Image 2",m2)
cv2.imshow("Image 3",m3)


cv2.waitKey()

cv2.destroyAllWindows()