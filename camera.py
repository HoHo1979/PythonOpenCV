import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pytesseract as pt
from pyzbar import pyzbar
import flask



server=flask.Flask("Test",template_folder="template/")

@server.route("/",methods=["GET"])

def page():
	return flask.render_template("shree/camera.html",openCamera="openCamera",closeCamera="closeCamera")
i=0
@server.route("/openCamera",methods=["GET","POST"])
def openCamera():
	global i 
	i+=1
	# flask.request.files["image"].save("template/shree/image2/"+str(i)+".jpg")
	m1=Image.open(flask.request.files["image"].stream)
	m1=np.array(m1)
	ret2=pyzbar.decode(m1)
	text=""
	for i in ret2:
		try:
			text = i.data.decode("utf-8").encode("sjis").decdoe("utf-8")+"<br>"
		except:
			text = i.data.decode("utf-8")+"<br>"	
	return "辨識結果:<br>" + text

@server.route("/closeCamera",methods=["GET","POST"])
def closeCamera():
	return ""
	
server.run(host="10.2.3.3",port=443,ssl_context="adhoc")

