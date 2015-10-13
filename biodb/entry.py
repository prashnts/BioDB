from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')

db = MongoEngine(app)

from user import controller
from security import controller
# from admin import controller


@app.route('/')
def home():
    return "LOL"

if __name__ == '__main__':
    app.run()
