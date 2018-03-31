
HRIDHYANAM
To automatically detect the presence of Cardiomegaly by processing an X-Ray of thoracic cavity.

Getting Started

Prerequisites

Install the following libraries and softwares:

Matlab 
Python-flask
Anaconda
Tensorflow
Tflearn
OpenCV
Flask-uploads
Xampp

Installing


The following softwares can be downloaded from the available links below:

Anaconda :
https://www.anaconda.com/download/

Python-flask :
https://pypi.python.org/pypi/Flask

Matlab : 
https://matlab.en.softonic.com/

Tensorflow :
https://www.tensorflow.org/
https://www.apachefriends.org/download.html

The following command can be used to install the flaask libraries

Pip install flask-uploads

OpenCV:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html

Running the tests

On the server side , first create and activate the tensorflow environment for executing the deep learning model.
Activate the flask server using Python app.py command.
Now the user can upload all the images of an x-ray on the web application and get the report generated with the dashboard full of the statistics.
The web application has the ability to the accept the multiple file uploads.
The images that are uploaded are of .png type and then the image processing is done on these images. 
The deep learning model is trained using these images after the preprocessing and generate the following reports.
The system also supports batch processing.


Running the tests
On the server side , first create and activate the tensorflow environment for executing the deep learning model.
Activate the flask server using Python app.py command.
Now the user can upload all the images of an x-ray on the web application and get the report generated with the dashboard full of the statistics.
The web application has the ability to the accept the multiple file uploads.
The images that are uploaded are of .png type and then the image processing is done on these images. 
The deep learning model is trained using these images after the preprocessing and generate the following reports.
The system also supports batch processing.
