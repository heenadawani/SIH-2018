from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
from deeplearning.predict import deepLearning
import os

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(app, photos)

@app.route('/')
def index():
    return render_template('index.html')

#uploading a file to the folder
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        result=deepLearning()
        os.system('cls')
    return render_template('report.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)