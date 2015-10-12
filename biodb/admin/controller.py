#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView
from flask_admin import helpers as admin_helpers

from user.model import Role, User

from app import app

admin = Admin(app, name='BioDB Admin', template_mode='bootstrap3', base_template='my_master.html')

admin.add_view(ModelView(User))
admin.add_view(ModelView(Role))
