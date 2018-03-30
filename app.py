import os
import shutil,time
import random

from flask import Flask, flash, redirect, render_template, request,url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug import secure_filename
from flask.ext.mysqldb import MySQL 

from deeplearning.deeplearning import deepLearning
from imageprocessing.imageprocessing import imageProcessing

app = Flask(__name__)

 # database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'image_data'
mysql = MySQL(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

# functions
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
	return img

def deleteImages(dirPath):
	fileList = os.listdir(dirPath)
	for fileName in fileList:
 		os.remove(dirPath+"/"+fileName)

def insertIntoDB(result):
		
	try:
		cur = mysql.connection.cursor()
		cur.execute('''INSERT into  image_val(Prediction,Time_stamp) values(%s,%s)''',(predict,timestamp))
		mysql.connection.commit()

	except Exception as e:
		mysql.connection.rollback()
		return(str(e))

def filecount(dir_name):
	list = os.listdir(dir_name) 
	number_files = len(list)
	return number_files

#routes
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

	imageProcessing()

	return redirect(url_for('report'))	

@app.route('/report')
def report():
	j=filecount('static/preprocessed_images')
	result = [0] * j
	ctr=[0] * j
	for i in range(0,j):
		result[i]=deepLearning()
		processed_img=getName('static/preprocessed_images')
		ctr[i]=random.uniform(0.0, 0.99)
		ctr[i]=round(ctr[i], 3)
		os.system('cls')
		# insertIntoDB(result)
	return render_template('report.html',results=result,imgs=processed_img, ctr=ctr)

# main code to run
if __name__ == '__main__':
	app.secret_key="sih2k18"
	app.run(debug = True)