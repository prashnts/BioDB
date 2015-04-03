#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

#from flask import Flask, Blueprint, render_template

#user = Blueprint("user", __name__, template_folder = "view")

from hashids import Hashids
import utils

class Instance:
    def __init__(self, user_name):
        self.udb = utils.Database.user
        if _Utils.user_exists(user_name):
            self.user_name = user_name
            user_dat = self.udb.find_one({"user_name": user_name})
        pass


class _Utils:
    def user_exists(self, user_name):
        return utils.Database.user.find_one({"user_name": user_name})

    def email_exists(self, email_id):
        return utils.Database.user.find_one({"email_id": email_id})

    def pswd_compare(self, pswd_one, pswd_two):
        pass

class User:
    def __init__(self, mode = "", user_name = None):
        """Initializes the instance as *mode*"""
        pass

    def add(
        self,
        user_name,
        password,
        confirm_password,
        email_id):
        """Adds the User into Database."""
        self.udb = utils.Database.user

        if udb.find_one({"user_name": user_name}):
            return (False, "UsernameExist")
        elif udb.find_one({"email_id": email_id}):
            return (False, "EmailExist")
        elif password is not confirm_password:
            return (False, "PasswordNoMatch")

    def delete(self, user_name):
        """Deletes the User from Database."""
        pass

    def get_user_from_id(self, user_name):
        pass

    def get_user_from_user_name():
        pass

class Session:
    def login(self, user_name, pswd):
        if not _Utils.user_exists(user_name):
            return False
        pass

    def logout(self, session_id, session_key):
        pass

    def check(self, session_id, session_key):
        pass

    def _create(self, user_name):
        """Creates a new session for the user."""
        pass

    def _verify(self, user_name, session_id, session_key):
        """Checks the session ID, validity, and integrity."""
        pass

    def _delete(self, user_name, session_id = False):
        """Deletes the session ID, and logs a log-out event."""
        pass

    def _keygen(self, entropy):
        pass

