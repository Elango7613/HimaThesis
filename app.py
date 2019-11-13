import os
#import magic
import urllib.request
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import json
from model import age_gender_detector

UPLOAD_FOLDER = 'C:/Users/elang/Desktop/DBS/Hima-Joythi/AgeFinder-WebApp/model/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadinputimage',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            #print(f'Result File:{age_gender_detector.executeModel(filename)}')
            return age_gender_detector.executeModel(filename)
            #return redirect('/')
        else:
            flash('Allowed file types are png, jpg, jpeg')
            return redirect(request.url)
        #

if __name__ == "__main__":
    app.debug = True
    app.run()