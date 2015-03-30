#!/env/bin python3

import flask

app.route("/", )

@route("/")
def init():
    return "Index Page"

@route("/login/:destination")
def login(destination):
    if destination == "admin":
        # intit admin login
    elif destination == "user":
        # inti user login
    else:
        # throw error

@get("/database/add")
def show_db_addition_interface():
    return False

@post("database/add")
def add_into_database():
    return False
