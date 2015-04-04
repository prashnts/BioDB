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

class Instance(object):
    """
    The User Class.
    """
    def __init__(self, user_name):
        if _Utils.user_exists(user_name) is False:
            self.k = False
            return None
        self.k = True
        self.udb = utils.Database().user
        self._user_dat = self.udb.find_one({"user_name": user_name})
        self._updates = set()

    @property
    def email(self):
        return self._user_dat['email']

    @email.setter
    def email(self, value):
        if _Utils.validate_email(value) is True:
            self._updates.add('email')
            self._user_dat['email'] = value
        else:
            pass

    @property
    def user_name(self):
        return self._user_dat['email']

    @property
    def session(self):
        return self._user_dat['session'] if 'session' in self._user_dat else {}

    @session.setter
    def session(self, value):
        self._updates.add('session')
        self._user_dat['session'] = value

    @property
    def pswd(self):
        return self._user_dat['pswd']

    @pswd.setter
    def pswd(self, value):
        if _Utils.validate_password(value) is True:
            self._updates.add('pswd')
            self._user_dat['pswd'] = Password.get_hashed_password(value)
        else:
            pass

    @property
    def status(self):
        return self._status if 'status' in self._user_dat else 0

    @status.setter
    def status(self, value):
        if value in [0, 1, 2, 3]:
            self._updates.add('status')
            self._user_dat['status'] = value
        else:
            pass

    def update(self):
        for change in self._updates:
            self.udb.update(
                {'user_name': self._user_dat['user_name']},
                {'$set': {change: self._user_dat[change]}},
                upsert = False,
                multi = False)

    def __del__(self):
        self.update();


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

        if _Utils.validate_username(user_name) is False:
            errors.append("BadUserName")

        if _Utils.validate_email(email_id) is False:
            errors.append("BadEmailID")

        if _Utils.validate_password(password) is False:
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

    def delete(user_name):
        """Deletes the User from Database."""
        user = Instance(user_name)
        if user.k is True:
            # 0 is a code for Deleted user.
            user.status = 0

class Session:
    def login(self, user_name, pswd):

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
        # Check hashed password. Using bcrypt, the salt is saved into the hash itself
        return bcrypt.checkpw(plain_text_password, hashed_password)

#print(Manage.add("prashant", "para-xylene", "para-xylene", "me@prshnts.in"))
ps = Instance("prashant")
ps.status = 3