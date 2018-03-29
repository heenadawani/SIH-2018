import numpy as np
import cv2
from matplotlib import pyplot as plt
import bisect
import random
import os



def imageProcessing():
	k=0
	var="D:\\code\\SIH-2018\\static\\uploads"
	emp="D:\code\SIH-2018\static\\preprocessed"
	
	for img in os.listdir(var):
		path=os.path.join(var,img)
		im = cv2.imread(path,0)
		equ = cv2.equalizeHist(im)
		ret,imgf=cv2.threshold(equ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		img1=cv2.bitwise_not(imgf)
		cv2.imwrite(path,img1)
		new=str(k)+".png"
		newpath=os.path.join(emp,new)
		os.rename(path,newpath)
		k=k+1