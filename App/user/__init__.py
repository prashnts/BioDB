#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask import Flask, Blueprint, render_template

from . import model

usr = Blueprint('usr', __name__, template_folder='templates')

@usr.route('/')
def get():
    return "Test"
