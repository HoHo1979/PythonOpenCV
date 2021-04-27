import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pytesseract as pt
from pyzbar import pyzbar
import flask

# server=flask.Flask("Test",template_folder="template/shree/")

# @server.route("/",methods=["GET"],defaults={"page":1})
# @server.route("/<int:page>")
# def home(page):
# 	return "Page"+" "+str(page)

# server.run(host="10.2.3.3",port=443,ssl_context="adhoc")

server=flask.Flask("Test",template_folder="template/")

@server.route("/",methods=["GET"],defaults={"file":"index.html"})
@server.route("/<path:file>",methods=["GET"])
def home(file):
	if ".png" in file or ".jpg" in file or ".gif" in file:
		return flask.send_from_directory("template/shree/",file,as_attachment=False)
	else:
		r=flask.make_response(flask.render_template("shree/"+file))
		if ".html" in file:
			r.headers["content-type"]="text/html"
		elif ".css" in file:	
			r.headers["content-type"]="text/css"
		elif ".js" in file:	
			r.headers["content-type"]="text/javascript"
		return r

server.run(host="10.2.3.3",port=443,ssl_context="adhoc")