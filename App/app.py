from flask import Flask, render_template, request, jsonify
from user import usr
from biodb import biodb
from config import config

import json

app = Flask(__name__)
app.register_blueprint(usr, url_prefix = '/usr')
app.register_blueprint(biodb, url_prefix = '/db')

@app.route('/add', methods=['POST','GET'])
def index():
	return render_template('add.html')

@app.route('/db/add', methods=['POST'])
def add():
	print(request.form)
	
	response = {
		'status' : "ok",
		'message' : "Today is Pizza Hut's unlimited day!"
	}
	return jsonify(response), 200


if __name__ == "__main__":
    app.run(host = config['HOST'], port = config['PORT'], debug = config['DEBUG'])