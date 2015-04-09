#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask import Flask, Blueprint, render_template, request, jsonify

from user import model as user_model

db = Blueprint('db', __name__, template_folder='templates')

@db.route('/')
def get():
    return "Test"
