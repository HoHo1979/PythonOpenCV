import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pytesseract as pt
from pyzbar import pyzbar

# print("test...")

# m1 = cv2.imread("paperwork.png",1)

# m1 = cv2.cvtColor(m1,cv2.COLOR_BGR2GRAY)

# print(m1)

# m1 = cv2.cvtColor(m1,cv2.COLOR_GRAY2BGR)

# print(m1)


# cv2.imshow("Image 1",m1)

# cv2.imwrite("1.png",m1)

# cv2.imwrite("1.jpg",m1,[cv2.IMWRITE_JPEG_QUALITY, 100])

# cv2.waitKey(0)

# cv2.destroyAllWindows()


# print("高",m1.shape[0])
# print("寬",m1.shape[1])

# # 灰階沒有第三維,有下面會出錯
# print("色彩空間",m1.shape[2])

# p1=cv2.VideoCapture("abc.mp4")

# 讀取QRCODE
p1=cv2.VideoCapture(0)
# print("寬度",p1.get(3))
# print("高度",p1.get(4))
# print("每秒影格數",p1.get(5))
# p1.set(1,6000)

w=int(p1.get(3))
h=int(p1.get(4))

# r1=cv2.VideoWriter("1.mp4", cv2.VideoWriter_fourcc(*'MP4V'),30, (w,h))

while p1.isOpened()==True:
	ret,m1=p1.read()

	if ret == True:
		# r1.write(m1)

		ret1=pyzbar.decode(m1)
		for i in ret1:
			print("類型",i.type)
			try:
				text=i.data.decode("utf-8").encode("sjis").decode("utf-8")
				print("內容",i.data.decode("utf-8").encode("sjis").decode("utf-8"))
			except:
				text=i.data.decode("utf-8")
				print("內容",i.data.decode("utf-8"))
			
			x,y,w,h=i.rect
			m1=Image.fromarray(m1)
			ImageDraw.Draw(m1).text((x,y),text,(0,0,255),ImageFont.truetype("arial.ttf",16))
			m1=np.array(m1)
			cv2.rectangle(m1,(x,y),(x+w,y+h),(0,255,0),2)
		

			print("位置",i.rect)
			
		# print("當前影格",p1.get(1),"影片總影格",p1.get(7))
		cv2.imshow("Image 1",m1)
		if cv2.waitKey(33)!=-1:
			break
	else:
		break


ret.release()

