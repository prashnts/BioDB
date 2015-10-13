#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from flask.ext.security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user

from entry import app
from user.model import User, Role

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )
