import matlab.engine
import os as os

def getName():
	paths='D:\code\SIH-2018\static\preprocessed_images'
	name=[]
	for i in os.listdir(paths):
		name.append(i)
	return name

eng = matlab.engine.start_matlab()
a=getName()
paths='D:\code\SIH-2018\static\preprocessed_images'
for i in range(len(a)):
	a[i]=os.path.join(paths,a[i])
	ctr = eng.automationgg(a[i],nargout=1)
	print(ctr)