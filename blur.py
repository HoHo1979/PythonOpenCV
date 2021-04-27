import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

m1 = cv2.imread("lafite.jpg",0)

m2 = cv2.blur(m1,(31,31))

m3 = cv2.medianBlur(m1,3)

cv2.imshow("Image 1",m1)
cv2.imshow("Image 2",m2)
cv2.imshow("Image 3",m3)


cv2.waitKey()

cv2.destroyAllWindows()