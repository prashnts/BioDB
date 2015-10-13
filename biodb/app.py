from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView
from flask_admin import helpers as admin_helpers

# Create app
app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')

# Create database connection object
db = MongoEngine(app)

# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
