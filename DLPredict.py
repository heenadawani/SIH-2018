import numpy as np
import cv2
import os as os

img_size = 128
lr = 1e-3
img_test= 'E:\data\images_001\local_demo'

model_name="PA-{}-{}-{}.model".format(lr,'8tryconv-basic-project',img_size)

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

import tensorflow
tensorflow.reset_default_graph()

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
convnet = dropout(convnet, 0.4)

convnet = fully_connected(convnet, 2, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=lr, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet, tensorboard_dir='log')

model.save(model_name)
def label_img(img):
    #word_label=img.split('.')[-3]
    if img=='Cardiomegaly' : return [1,0]
    elif img=='No Cardiomegaly' : return [0,1]
    
    
def create_img_test_data(): 
    img_testing_data=[]
    #count=0
    for img in os.listdir(img_test):

        path=os.path.join(img_test,img)
        img=cv2.resize(cv2.imread(path,cv2.IMREAD_GRAYSCALE),(img_size,img_size))
        img_testing_data.append([np.array(img)])

    np.save('new_img_test_data_trainDown.npy',img_testing_data)
    return img_testing_data

create_img_test_data()

test_img=np.load('new_img_test_data_trainDown.npy')

import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15,15)

for num,data in enumerate(test_img[:]):

    count=0
    #img_num = data[1]
    img_data = data[0]

    orig = img_data
    data = img_data.reshape(img_size,img_size,1)

    model_out = model.predict([data])[0]
    
    if np.argmax(model_out) == 1: str_label='No Cardiomegaly'
    else: str_label='Cardiomegaly'
        
    print(str_label)