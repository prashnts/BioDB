#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

#from flask import Flask, Blueprint, render_template

#user = Blueprint("user", __name__, template_folder = "view")

# Global imports
import bcrypt
import datetime
from hashids import Hashids

# Local imports
import utils

class Instance:
    def __init__(self, user_name):
        self.udb = utils.Database().user
        if _Utils.user_exists(user_name):
            self.user_name = user_name
            user_dat = self.udb.find_one({"user_name": user_name})
        pass


class _Utils:
    def user_exists(user_name):
        return utils.Database().user.find_one({"user_name": user_name}) is not None

    def email_exists(email_id):
        return utils.Database().user.find_one({"email": email_id})

    def validate_username(user_name):
        pass

    def validate_password(password):
        pass

    def validate_email(email_id):
        pass

class Manage:
    def add(
        user_name,
        password,
        confirm_password,
        email_id):
        """Adds the User into Database."""
        if _Utils.user_exists(user_name):
            return (False, "UsernameExist")
        elif _Utils.email_exists(email_id):
            return (False, "EmailExist")
        elif password is not confirm_password:
            return (False, "PasswordNoMatch")

        user = {
            'user_name': user_name,
            'pswd': Password.get_hashed_password(password),
            'email': email_id,
            'status': 1,
            'meta': {
                'added': datetime.datetime.utcnow()
            }
        }

        return utils.Database().user.insert_one(user).inserted_id

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


class Password:
    def get_hashed_password(plain_text_password):
        # Hash a password for the first time
        #   (Using bcrypt, the salt is saved into the hash itself)
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def check_password(plain_text_password, hashed_password):
        # Check hased password. Useing bcrypt, the salt is saved into the hash itself
        return bcrypt.checkpw(plain_text_password, hashed_password)

print(Manage.add("pjraaa", "jaisubaby", "jaisubaby", "pragya.jswl@gmail.com"))