#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask import Flask, Blueprint, render_template, request, jsonify

from . import model as user_model

usr = Blueprint('usr', __name__, template_folder='templates')

@usr.route('/')
@user_model.logged_in
def get():
    return "Test"

@usr.route('/login', methods = ['POST'])
def login():
    if all([
        'user_name' in request.form,
        'password'  in request.form
    ]):
        user_name = request.form['user_name']
        password = request.form['password']
        res = user_model.Session.login(user_name, password)
        if res[0] is True:
            "Logged in, send the tokens back. Also, set the cookie."
            response = {
                'error': False,
                'user_id': res[1],
                'user_token': res[2]
            }
            return jsonify(response), 200
        else:
            "Nope, couldnt login. Error."
            response = {
                'error': True,
                'message': "Authentication Error."
            }
            return jsonify(response), 401

    response = {
        'error': True,
        'message': "Missing `user_name` | `password`"
    }
    return jsonify(response), 400

@usr.route('/logout', methods = ['GET'])
@user_model.logged_in
def logout():
    return "done"