import numpy as np
import cv2
from matplotlib import pyplot as plt
import bisect

im = cv2.imread('xray.png',0)
height = np.size(im, 0)
width = np.size(im, 1)

#print(height,width)
#this is noise introduction
#im = cv2.medianBlur(im,7)
im = cv2.equalizeHist(im)
# Create the basic black image 
mask = np.zeros(im.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
cv2.rectangle(mask, (0, 300), (width, height-300), (255, 255, 255), -1)

#apply mask and display image
maskedImg = cv2.bitwise_and(im, mask)

final=maskedImg.copy()
#imadjust function of matlab
def imadjust(src, tol, vin=[0,255], vout=[0,255]):
    # src : input one-layer image (numpy array)
    # tol : tolerance, from 0 to 100.
    # vin  : src image bounds
    # vout : dst image bounds
    # return : output img

    dst = src.copy()
    tol = max(0, min(100, tol))

    if tol > 0:
        # Compute in and out limits
        # Histogram
        hist = np.zeros(256, dtype=np.int)
        for r in range(src.shape[0]):
            for c in range(src.shape[1]):
                hist[src[r,c]] += 1
        # Cumulative histogram
        cum = hist.copy()
        for i in range(1, len(hist)):
            cum[i] = cum[i - 1] + hist[i]

        # Compute bounds
        total = src.shape[0] * src.shape[1]
        low_bound = total * tol / 100
        upp_bound = total * (100 - tol) / 100
        vin[0] = bisect.bisect_left(cum, low_bound)
        vin[1] = bisect.bisect_left(cum, upp_bound)

    # Stretching
    scale = (vout[1] - vout[0]) / (vin[1] - vin[0])
    for r in range(dst.shape[0]):
        for c in range(dst.shape[1]):
            vs = max(src[r,c] - vin[0], 0)
            vd = min(int(vs * scale + 0.5) + vout[0], vout[1])
            dst[r,c] = vd
    return dst

#function call
vincall = [0,255]
voucall = [15,180]
var=imadjust(final,25,vincall,voucall)

#this is histogram
#hist_full = cv2.calcHist([im],[0],None,[256],[0,256])

#this is thresholding
#ret,thresh = cv2.threshold(var,100,255,cv2.THRESH_BINARY_INV)
th2 = cv2.adaptiveThreshold(var,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

#canny edge detection
#edges = cv2.Canny(th2,100,200)

#introducing noise again
#newnoise = cv2.medianBlur(edges,1)
#doing the AND operation
#final = cv2.bitwise_and(edges,newnoise)

#find contours
#image, contours, hierarchy = cv2.findContours(final,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#draw contours not working
#cnt = contours[4]
#finalim = cv2.drawContours(final, [cnt], 0, (0,255,0), 3)

#this is display
titles = ['Original Image','adjust image']
images = [im,th2]
for i in xrange(2):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
#cv2.imshow('image',im)
#cv2.waitKey(0)
#cv2.destroyAllWindows()