from __future__ import print_function
from flask import Flask
from flask import render_template, flash, redirect, request, jsonify
from preprocessor import Preprocessor as img_prep
import json
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	app.logger.debug("Went to OCR page")
	return render_template('index.html', title='Optical Character Recognition', prediction=None)

@app.route('/_do_recognition', methods=['GET', 'POST'])
def do_recognition():
	app.logger.debug("Accessed _do_ocr page with image data")
	# flash('Just hit the _add_numbers function')
	# a = json.loads(request.args.get('a', 0, type=str))
	data = request.args.get('imgURI', 0, type=str)
	app.logger.debug("Data looks like " + data)
	index = request.args.get('index', 0, type=int)
	vocab = json.loads(request.args.get('vocab',0,type=str))
	img = img_prep().preprocess(data)
	print(img)
	#pp = img_prep(fn="dataset.txt")
	#ocr = LiteOCR(fn="app/model/alpha_weights.pkl")
	#char_prediction= ocr.predict(pp.preprocess(data))

	result = "You entered a: " + char_prediction

	app.logger.debug("Recognized a character")
	return jsonify(result=result)



if __name__ == '__main__':
    app.run(debug=True)
