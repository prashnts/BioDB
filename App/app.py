from flask import Flask, render_template, request, jsonify
from user import usr
from biodb import biodb
from config import config

import json

app = Flask(__name__)
app.register_blueprint(usr, url_prefix = '/usr')
app.register_blueprint(biodb, url_prefix = '/app')

@app.route('/add', methods=['POST','GET'])
def addPage():
	return render_template('add.html')

@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')


if __name__ == "__main__":
    app.run(host = config['HOST'], port = config['PORT'], debug = True)