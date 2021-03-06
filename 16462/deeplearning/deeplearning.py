def deepLearning():

	import os as os
	import cv2
	import numpy as np

	img_size =50
	lr = 1e-3
	epoch=100
	step=500

	img_test_dir='D:\\code\\16462\\static\\preprocessed_images'

	model_name="D:\\code\\16462\\deeplearning\\Processed_PA-0.001-8tryconv-basic-project-50.model"

	import tflearn
	from tflearn.layers.conv import conv_2d, max_pool_2d
	from tflearn.layers.core import input_data, dropout, fully_connected
	from tflearn.layers.estimator import regression

	import tensorflow as tf

	tf.reset_default_graph()

	convnet = input_data(shape=[None, img_size, img_size, 1], name='input')

	convnet = conv_2d(convnet, 32, 5, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = conv_2d(convnet, 64, 5, activation='relu')
	convnet = max_pool_2d(convnet, 2)


	convnet = conv_2d(convnet, 32, 5, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = conv_2d(convnet, 64, 5, activation='relu')
	convnet = max_pool_2d(convnet, 2)


	convnet = conv_2d(convnet, 32, 5, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	
	convnet = conv_2d(convnet, 64, 5, activation='relu')
	convnet = max_pool_2d(convnet, 2)


	convnet = conv_2d(convnet, 32, 5, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = conv_2d(convnet, 64, 5, activation='relu')
	convnet = max_pool_2d(convnet, 2)


	convnet = fully_connected(convnet, 1024, activation='relu')
	convnet = dropout(convnet, 0.5)

	
	convnet = fully_connected(convnet, 2, activation='softmax')
	convnet = regression(convnet, optimizer='adam', learning_rate=lr, loss='categorical_crossentropy', name='targets')

	model = tflearn.DNN(convnet, tensorboard_dir='log')


	model.load(model_name)

	def label_img(img):
	    #word_label=img.split('.')[-3]
	    if img=='Cardiomegaly' : return [1,0]
	    elif img=='No Cardiomegaly' : return [0,1]
	    
	    
	def create_img_test_data(): 
	    img_testing_data=[]
	    #count=0
	    for img in os.listdir(img_test_dir):

	        path=os.path.join(img_test_dir,img)
	        img=cv2.resize(cv2.imread(path,cv2.IMREAD_GRAYSCALE),(img_size,img_size))
	        img_testing_data.append([np.array(img)])

	    np.save('new_img_test_data_trainDown.npy',img_testing_data)
	    return img_testing_data

	create_img_test_data()

	test_img=np.load('new_img_test_data_trainDown.npy')

	# import matplotlib.pyplot as plt

	# plt.rcParams['figure.figsize'] = (15,15)

	result=[]

	for num,data in enumerate(test_img[:]):

	    count=0
	    #img_num = data[1]
	    img_data = data[0]

	    orig = img_data
	    data = img_data.reshape(img_size,img_size,1)

	    model_out = model.predict([data])[0]
	    
	    if np.argmax(model_out) == 1: str_label='No Cardiomegaly'
	    else: str_label='Cardiomegaly'
	        
	    result.append(str_label)

	return result	    
	# print(result)   
# deepLearning()