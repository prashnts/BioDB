#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

#from flask import Flask, Blueprint, render_template

#user = Blueprint("user", __name__, template_folder = "view")

# Global imports
import bcrypt
import datetime
import re
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
        min_len = 3
        max_len = 32

        pattern = r"^(?i)[a-z0-9_-]{%s,%s}$" %(min_len, max_len)
        return bool(re.match(pattern, user_name)) == True

    def validate_password(password):
        return len(password) > 5

    def validate_email(email_id):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return bool(re.match(pattern, email_id)) == True

class Manage:
    def add(
        user_name,
        password,
        confirm_password,
        email_id):
        """Adds the User into Database."""
        errors = []

        if _Utils.validate_username(user_name) is not True:
            errors.append("BadUserName")

        if _Utils.validate_email(email_id) is not True:
            errors.append("BadEmailID")

        if _Utils.validate_password(password) is not True:
            errors.append("ShortPassword")

        if _Utils.user_exists(user_name):
            errors.append("UsernameExist")

        if _Utils.email_exists(email_id):
            errors.append("EmailExist")

        if password is not confirm_password:
            errors.append("PasswordNoMatch")

        if len(errors) is not 0:
            return (False, errors)
        else:
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

#print(Manage.add("prashant", "para-xylene", "para-xylene", "me@prshnts.in"))