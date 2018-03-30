import numpy as np
import cv2
import os

def imageProcessing():

	var="D:\\code\\SIH-2018\\static\\normal_images"
	emp="D:\\code\\SIH-2018\\static\\preprocessed_images"
	
	for img in os.listdir(var):
		path=os.path.join(var,img)
		im = cv2.imread(path,0)
		equ = cv2.equalizeHist(im)
		ret,imgf=cv2.threshold(equ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		img1=cv2.bitwise_not(imgf)
		cv2.imwrite(path,img1)
		newpath=os.path.join(emp,img)
		os.rename(path,newpath)