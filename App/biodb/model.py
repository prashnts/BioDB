#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

# Local imports
import utils

class Software(object):
    def add(software_name, tags, primary_link, one_liner, paid, primary_ref = "N.A", remarks = "N.A", meta = None):
        """
        Adds the software into the Database. Any additional properties should
        only be added into `meta`.
        """
        if all([
            type(software_name) is str,
            type(tags) is list,
            type(primary_link) is str,
            type(one_liner) is str,
            type(paid) is bool,
            type(primary_ref) is str,
            type(remarks) is str,
            type(meta) is dict or meta is None
        ]):
            sw = {
                "software_name": software_name,
                "tags": tags,
                "primary_link": primary_link,
                "one_liner": one_liner,
                "paid": paid,
                "primary_ref": primary_ref,
                "remarks": remarks,
                "meta": meta
            }

            return utils.Database().biodb.insert_one(sw).inserted_id

        return None

    def delete(software_id):
        utils.Database().biodb.remove({'_id': software_id}, True)

    def update(
            software_id,
            software_name = None,
            primary_link = None,
            one_liner = None,
            paid = None,
            primary_ref = None,
            remarks = None,
            meta = None
        ):

        update = {}

        def __update_macro(key, type):
            val = eval(key)
            if all([
                val is not None,
                type(val) is str
            ]):
                update[key] = val

        __update_macro('software_name', str)
        __update_macro('primary_link', str)
        __update_macro('one_liner', str)
        __update_macro('paid', bool)
        __update_macro('primary_ref', str)
        __update_macro('remarks', str)
        __update_macro('meta', dict)

        if len(update) is not 0:
            utils.Database().biodb.update(
                {'software_id': software_id},
                {'$set': update},
                upsert = False,
                multi = False
            )
            return True

        return False

class Feed(object):
    def create(page = 0, tags = None):
        pass
