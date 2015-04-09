from flask import Flask, render_template, request, jsonify
from user import usr
from biodb import biodb
from config import config

app = Flask(__name__)
app.register_blueprint(usr, url_prefix = '/usr')

@app.route('/add')
def index():
	name = "devesh"
	return render_template('add.html')

@app.route('/submit', methods=['POST'])
def add():
	print(request.form['url'])
	print(request.form['name'])
	print(request.form['license'])
	response = {
		'status' : "ok",
		'message' : "Tomorrow is Pizza Hut's unlimited day!"
	}
	return jsonify(response), 200

if __name__ == "__main__":
    app.run(host = config['HOST'], port = config['PORT'], debug = config['DEBUG'])