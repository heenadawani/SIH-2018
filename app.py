import os
import shutil

from flask import Flask, flash, redirect, render_template, request,url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug import secure_filename
from flask_mysqldb import MySQL

from deeplearning.deeplearning import deepLearning
from imageprocessing.imageprocessing import imageProcessing

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def copyImages():
	dir_src = ("static/normal_images/")
	dir_dst = ("static/repository/")

	for filename in os.listdir(dir_src):
	    if filename.endswith('.png'):
	        shutil.copy( dir_src + filename, dir_dst)

def getName(path):
	img=os.listdir(path)
	return img[0]

def deleteImages(dirPath):
	fileList = os.listdir(dirPath)
	for fileName in fileList:
 		os.remove(dirPath+"/"+fileName)

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/uploader', methods = ['POST'])
def uploader():

	deleteImages("static/preprocessed_images")

	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)

	for f in request.files.getlist('file'):
		UPLOAD_FOLDER = 'static/normal_images'
		app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		copyImages()

	imageProcessing() #this will also empty the normal_images folder

	return redirect(url_for('report'))	

@app.route('/report')
def report():

	img=getName('static/preprocessed_images')
	result=deepLearning()
	os.system('cls')

	return render_template('report.html',result=result,img=img)

if __name__ == '__main__':
	app.secret_key="sih2k18"
	app.run(debug = True)

#images should also get deleted after the work is done from normal images and preprocessed_images --done
#insert the uploaded file into the 1.normal_images and 2.repository --done
#render the processed image instead of dummy image from the database --done

#rename images after uploading them into the repository // will need database
#add the image details into the 3.database // will need database	
#pass k as a parameter to rename the file. //will require database
#insert the result into the table //will require database