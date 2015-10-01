from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required
from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView

# Create app
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

# MongoDB Config
app.config['MONGODB_DB'] = 'mydatabase'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config['SECURITY_REGISTERABLE'] = True

# Create database connection object
db = MongoEngine(app)

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    username = db.StringField(max_length=40)
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])
    tags = db.ListField(db.ReferenceField('Tag'))

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    user_datastore.create_user(email='matt@nobien.net', password='password')

# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')

admin = Admin(app, name='microblog', template_mode='bootstrap3')

class Software(db.Document):
    name = db.StringField(max_length=40)
    tags = db.ListField(db.ReferenceField('Tag'))

class Tag(db.Document):
    name = db.StringField(max_length=40)

    def __unicode__(self):
        return self.name


class UserView(ModelView):
    column_filters = ['name']

    # column_searchable_list = ('name')

admin.add_view(UserView(Software))
admin.add_view(ModelView(Tag))
if __name__ == '__main__':
    app.run()
