import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pytesseract as pt

m1=  cv2.imread("abc.png")
text = pt.image_to_string(m1,"eng","-c tessedit_char_blacklist=BC")

print(text)

cv2.imshow("Image 1",m1)
cv2.waitKey(0)

cv2.destroyAllWindows()

