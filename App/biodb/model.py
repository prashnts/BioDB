#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

# Local imports
import utils

class Software(object):
    def add(software_name, tags, primary_link, one_liner, paid, primary_ref, remarks, meta = None):
        pass

    def delete(software_id):
        pass

    def update(
            software_id,
            _software_name = None,
            _primary_link = None,
            _one_liner = None,
            _paid = None,
            _primary_ref = None,
            _remarks = None,
            _meta = None
        ):
        pass

class Feed(object):
    def create(tags):
        pass