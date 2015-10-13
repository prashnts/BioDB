#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

DEBUG                   = True
SECRET_KEY              = 'super-secret'

# MongoDB Config
MONGODB_DB              = 'llo'
MONGODB_HOST            = 'localhost'
MONGODB_PORT            = 27017
SECURITY_REGISTERABLE   = True


# Flask_Security
SECURITY_PASSWORD_HASH  = 'pbkdf2_sha512'
SECURITY_CONFIRMABLE    = True
SECURITY_RECOVERABLE    = True
SECURITY_PASSWORD_SALT  = 'SUPER!'
