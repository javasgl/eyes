#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbm
from models.Config.Config import Config


class DBM(object):
    def __init__(self):
        self._db = dbm.open(Config.parse_config('dbm', 'dbfile'), 'c')

    def add(self, key, value):
        self._db[key] = str(value)
        return self

    def get(self, key):
        if key in self._db.keys():
            return self._db[key]
        else:
            return None

    def __del__(self):
        self._db.close()
        print 'close db'
