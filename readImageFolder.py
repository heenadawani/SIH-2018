'''import cv2
import os, os.path
#image path and valid extensions
imageDir = "E:\cardio532" #specify your path here
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

#create a list all files in directory and
#append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
	extension = os.path.splitext(file)[1]
	if extension.lower() not in valid_image_extensions:
		continue
	image_path_list.append(os.path.join(imageDir, file))

#loop through image_path_list to open each image
for imagePath in image_path_list:
	image=cv2.imread("E:\cardio")
	equ=cv2.equalizeHist(image)
	ret,imgf=cv2.threshold(equ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	img =cv2.bitwise_not(imgf)
	# display the image on screen with imshow()
	# after checking that it loaded
	if img is not None:
		cv2.imshow(image, i)
	elif img is None:
		print ("Error loading: " + image)
		#end this loop iteration and move on to next image
		continue
	
	# wait time in milliseconds
	# this is required to show the image
	# 0 = wait indefinitely
	# exit when escape key is pressed
	key = cv2.waitKey(0)
	if key == 27: # escape
		break

# close any open windows
cv2.destroyAllWindows()

from os import listdir
from os.path import isfile, join
import numpy
import cv2

mypath='E:/cardio'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
image= numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
	equ=cv2.equalizeHist(image)
	ret,imgf=cv2.threshold(equ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	img =cv2.bitwise_not(imgf)
  	images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
import cv2.cv as cv
import time

cv.NamedWindow("camera", 1)

capture = cv.CaptureFromCAM(0)
i = 0
while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    cv.SaveImage('pic{:>05}.jpg'.format(i), img)
    if cv.WaitKey(10) == 27:
        break
    i += 1
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
import bisect
import random
import numpy as np
import argparse
import imutils
import os
var="E:\\cardio_PA"
emp="E:\\cardio532"

for img in os.listdir(var):
	path=os.path.join(var,img)
	im = cv2.imread(path,0)
	equ = cv2.equalizeHist(im)
	ret,imgf=cv2.threshold(equ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	img1=cv2.bitwise_not(imgf)
	cv2.imwrite(path,img1)
	newpath=os.path.join(emp,img)
	os.rename(path,newpath)

