#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod
from models.DBM.DBM import DBM
import hashlib


class SpiderHandler(object):
    def __init__(self, handler=None):
        self._handler = handler

    def handle(self, params):
        processed = self.process(params)
        if processed is None:
            if self._handler is not None:
                processed = self._handler.handle(params)
        self.diff(params, processed)

    @abstractmethod
    def process(self, params):
        pass

    def diff(self, params, processed):
        if processed is not None:
            dbm = DBM()
            # diff rank
            md5 = hashlib.md5()
            md5.update(params)
            key = md5.hexdigest()
            previous_rank = dbm.get(key)
            if previous_rank is None:
                dbm.set(key, processed)
            else:
                previous_rank = int(previous_rank)
                processed = int(processed)

                if previous_rank > processed:
                    print '下降了'
                elif previous_rank < processed:
                    print '上升了'
                else:
                    print 'not changed'

        else:
            if self._handler is None:
                # last one handler is none , notify admin users
                print 'last one handler:%s' % type(self)
