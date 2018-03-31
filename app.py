import os
import shutil,time
import random
import matlab.engine

from flask import Flask, flash, redirect, render_template, request,url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug import secure_filename
from flask_mysqldb import MySQL 

from deeplearning.deeplearning import deepLearning

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
		if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.bmp'):
			shutil.copy( dir_src + filename, dir_dst)

def getName(path):
	img=os.listdir(path)
	return img

def deleteImages(dirPath):
	fileList = os.listdir(dirPath)
	for fileName in fileList:
 		os.remove(dirPath+"/"+fileName)

#make changes here to insert data into the table. Only for reference
def insertIntoDB(result):
	try:
		cur = mysql.connection.cursor()
		cur.execute('''INSERT into  image_val(classifier) values(%s)''',(predict))
		mysql.connection.commit()

	except Exception as e:
		mysql.connection.rollback()
		return(str(e))

def filecount(dir_name):
	list = os.listdir(dir_name) 
	number_files = len(list)
	return number_files


def automation():
	eng = matlab.engine.start_matlab()
	paths='D:\code\SIH-2018\static\preprocessed_images'
	name=[]
	ctr=[]
	for i in os.listdir(paths):
		name.append(i)
	
	for i in range(len(name)):
		name[i]=os.path.join(paths,name[i])
		ctr.append(eng.automationgg(name[i],nargout=1))
	return ctr

#routes
@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/uploader', methods = ['POST'])
def uploader():
	deleteImages("static/normal_images")
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

	os.chdir('imageprocessing')	
	os.system('python processing.py')

	return redirect(url_for('report'))	

@app.route('/report')
def report():
	os.chdir('D:\code\SIH-2018')
	j=filecount('static/preprocessed_images')
	result = [0] * j
	ctr=[]
	for i in range(0,j):
		result=deepLearning()
		processed_img=getName('static/preprocessed_images')

	ctr=automation()
	print(ctr)
		# os.system('cls')
		# insertIntoDB(result)
	return render_template('report.html',results=result,imgs=processed_img, ctr=ctr)

# main code to run
if __name__ == '__main__':
	app.secret_key="sih2k18"
	app.run(debug = True)