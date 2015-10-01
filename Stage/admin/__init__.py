#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask import Flask, Blueprint, render_template, request, jsonify
from flask_admin import Admin

adm = Blueprint('admin', __name__, template_folder='templates')

handle = Admin(adm, name='microblog', template_mode='bootstrap3')

