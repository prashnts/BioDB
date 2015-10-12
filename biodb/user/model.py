#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

import datetime

from flask.ext.security import UserMixin, RoleMixin
from biodb.app import db

class Role(db.Document, RoleMixin):
    #: Fine user permission control.

    name        = db.StringField(max_length = 80, unique = True)
    description = db.StringField(max_length = 255)

class User(db.Document, UserMixin):
    username        = db.StringField(max_length = 40, unique = True)
    email           = db.EmailField(max_length = 255, unique = True, required = True)
    password        = db.StringField(max_length = 255, required = True)
    active          = db.BooleanField(default = True)
    added           = db.DateTimeField(default = datetime.datetime.now)
    confirmed_at    = db.DateTimeField()
    roles           = db.ListField(db.ReferenceField(Role), default=[])
