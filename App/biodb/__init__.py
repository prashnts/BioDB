#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask import Flask, Blueprint, render_template, request, jsonify

from user import model as user_model

biodb = Blueprint('biodb', __name__, template_folder='templates')

@biodb.route('/')
def get():
    return "Test"
