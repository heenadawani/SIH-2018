import matlab.engine
import os

eng = matlab.engine.start_matlab()
a='D:\\code\\16462\\static\\normal_images'
b='D:\\code\\16462\\static\\preprocessed_images'

#matlabengine.matlabfun()

count=0
for img in os.listdir(a):
	count+=1

n=count
eng.processing(a,b,n,nargout=0)