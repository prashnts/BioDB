#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask.ext.mongoengine import MongoEngine

from .app import app

db = MongoEngine(app)

