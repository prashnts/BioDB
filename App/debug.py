from flask import Flask
from user import usr
from config import config

app = Flask(__name__)
app.register_blueprint(usr, url_prefix = '/usr')