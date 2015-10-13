#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask.ext.security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from flask_admin import helpers as admin_helpers

from entry import app, db
from user.model import User, Role
from admin.controller import admin

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# @security.context_processor
# def security_context_processor():
#     print("LOL")
#     return dict(
#         admin_base_template=admin.base_template,
#         admin_view=admin.index_view,
#         h=admin_helpers,
#     )
