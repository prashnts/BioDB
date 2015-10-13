from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')

db = MongoEngine(app)


def create_app():
    from user.controller import usr
    from security.controller import security
    from admin.controller import admin

    security.init_app(app)
    admin.init_app(app)
    app.register_blueprint(usr, url_prefix = '/usr')

@app.route('/')
def home():
    return "LOL"

if __name__ == '__main__':
    create_app()
    app.run()
