import os
from flask import Flask, flash, redirect, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
#from deeplearning.predict import deepLearning
from werkzeug import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	 return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    return render_template('report.html',result="Hey i am here.")
	
@app.route('/uploader', methods = ['POST'])
def uploader():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)

	for f in request.files.getlist('file'):
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return 'Image Upload Successful.'	

if __name__ == '__main__':
	app.secret_key="sih2k18"
	app.run(debug = True)