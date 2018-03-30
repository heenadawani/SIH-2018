import os
import shutil
import time
import datetime

from flask import Flask, flash, redirect, render_template, request,url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug import secure_filename
from flask.ext.mysqldb import MySQL 

from deeplearning.deeplearning import deepLearning
from imageprocessing.imageprocessing import imageProcessing

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'image_data'
mysql = MySQL(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def copyImages():
	dir_src = ("static/normal_images/")
	dir_dst = ("static/repository/")

	try:
		cur = mysql.connection.cursor()
		cur.execute('''SELECT MAX(id) FROM image_val''')
		maxid = cur.fetchone()
		
	except Exception as e:
		return(str(e))

	for filename in os.listdir(dir_src):
		if filename.endswith('.png'):
			shutil.copy( dir_src + filename, dir_dst)
		# print(maxid)
		# print(filename)
		# os.rename(maxid,filename)

def getName(path):
	img=os.listdir(path)
	return img[0]

def deleteImages(dirPath):
	fileList = os.listdir(dirPath)
	for fileName in fileList:
 		os.remove(dirPath+"/"+fileName)

def insertIntoDB(result):
	ts = time.time()
	
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	
	if result == "No Cardiomegaly":
		predict=0
	elif result == "Cardiomegaly":
		predict=1	
	
	try:
		cur = mysql.connection.cursor()
		cur.execute('''INSERT into  image_val(Prediction,Time_stamp) values(%s,%s)''',(predict,timestamp))
		mysql.connection.commit()

	except Exception as e:
		mysql.connection.rollback()
		return(str(e))

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

	processed_img=getName('static/preprocessed_images')
	result=deepLearning()
	os.system('cls')
	insertIntoDB(result)
	return render_template('report.html',result=result,img=processed_img)

if __name__ == '__main__':
	app.secret_key="sih2k18"
	app.run(debug = True)