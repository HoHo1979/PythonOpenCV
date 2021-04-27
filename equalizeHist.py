import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

m1 = cv2.imread("moutain.jpg",1)
m2 = m1.copy()

m2[:,:,0] = cv2.equalizeHist(m1[:,:,0])
m2[:,:,1] = cv2.equalizeHist(m1[:,:,1])
m2[:,:,2] = cv2.equalizeHist(m1[:,:,2])


cv2.imshow("Image 1",m1)
cv2.imshow("Image 2",m2)


cv2.waitKey()

cv2.destroyAllWindows()