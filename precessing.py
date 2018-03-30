import matlab.engine
import os
eng = matlab.engine.start_matlab()
a='E:\\source'
b='E:\\destination'

#matlabengine.matlabfun()

count=0
for img in os.listdir(a):
	count+=1

n=count
eng.precessing(a,b,n,nargout=0)
#print(count)
