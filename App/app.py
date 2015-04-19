from flask import Flask, render_template, request, jsonify
from user import usr
from biodb import biodb
from config import config

import json

app = Flask(__name__)
app.register_blueprint(usr, url_prefix = '/usr')
app.register_blueprint(biodb, url_prefix = '/db')
# app.register_blueprint(core, url_prefix = '/software')

@app.route('/add', methods=['POST','GET'])
def addPage():
	return render_template('add.html')

# @app.route('/software/<int:sw_id>', methods=['GET'])
# def software(sw_id):
# 	sw = biodb.Software(sw_id)
# 	return render_template('software.html')

# @app.route('/db/add', methods=['POST'])
# def add():
# 	print(request.form)
# 	manSW = biodb.model.Manage()
# 	manSW.addJSON(request.json)
# 	response = {
# 		'status' : "not ok",
# 		'message' : "I have to do this today!"
# 	}
# 	return jsonify(response), 200

@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')
	
if __name__ == "__main__":
    app.run(host = config['HOST'], port = config['PORT'], debug = config['DEBUG'])