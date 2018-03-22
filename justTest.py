import numpy as np
import cv2
from matplotlib import pyplot as plt
import bisect
import random
import argparse
from pylab import plot, ginput, show, axis

im = cv2.imread('D:\SIHIImageDataset/00000096_006.png',0)
#cv2.imshow('image',im)
refpt=[]
refpt1=[]
#enhancement
equ = cv2.equalizeHist(im)
#res = np.hstack((im,equ)) #stacking images side-by-side
#cv2.imwrite('res.png',res)
'''cv2.imshow('image',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#segmentation 
'''def sp_noise(image,prob):
   output = np.zeros(image.shape,np.uint8)
   thres = 1 - prob 
   for i in range(image.shape[0]):
       for j in range(image.shape[1]):
           rdn = random.random()
           if rdn < prob:
               output[i][j] = 0
           elif rdn > thres:
               output[i][j] = 255
           else:
               output[i][j] = image[i][j]
   return output
#image = cv2.imread('image.jpg',0) # Only for grayscale image
#noise_img = sp_noise(equ,0.05)
#cv2.imwrite('sp_noise.jpg', noise_img)
cv2.imshow('image',noise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

ret, imgf = cv2.threshold(equ, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)  #using otsu 

def MouseCallback(event,x,y,flag,param):
  if event == cv2.EVENT_LBUTTONDOWN:
    refpt = [(x,y)]
  if event == cv2.EVENT_RBUTTONDOWN:
    refpt1=[(x1,y1)]
  cv2.line(imgf,[(x,x1)],[(y,y1)],(255,0,0),3)
  #cv2.imshow('image',imgf)
  #distlung  = np.sqrt((x2-x1)**2 + (y1-y1)**2)
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',MouseCallback)
cv2.imshow('image',imgf)
#cv2.setMouseCallback('image',MouseCallback,2)

plt.subplot(1,2,1), plt.imshow(im,cmap = 'gray')
plt.title('Original Image')
plt.subplot(1,2,2), plt.imshow(imgf,cmap = 'gray')
plt.title('output Image')
plt.show()



