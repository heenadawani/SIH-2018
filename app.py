from flask import Flask,render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

photos=UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST']='C:\\Users\\Mansi\\Desktop\\UploadedImages'
configure_uploads(app, photos)

@app.route('/')
def index():
    return render_template('index.html')
	#return 'Hello World'

#uploading a file to the folder
@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST' and 'inputFile' in request.files:
        filename=photos.save(request.files['inputFile'])
        # alert('Uploaded succesfully')
        return filename
    return render_template('report.html')

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
