#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from bson.objectid import ObjectId
from flask import Flask, Blueprint, render_template, request, jsonify

from user import model as user_model
from . import model as biodb_model
from utils import validate_oid

biodb = Blueprint('biodb', __name__, template_folder='templates')

@biodb.route('/')
def get():
    return "Test"

@biodb.route('/software', methods = ['POST', 'PUT'])
def add():
    return "POTOLOLO"

@biodb.route('/software', methods = ['GET'])
def gets():
    return "LOL"

@biodb.route('/software/<oid>', methods = ['GET'])
@validate_oid
def get_software_detail(oid):
    return jsonify(biodb_model.Software(oid).hash), 200

@biodb.route('/software/<sw_id>', methods = ['POST'])
def update_software_detail(sw_id):

    pass