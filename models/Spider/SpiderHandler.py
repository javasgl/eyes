#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from abc import abstractmethod
from models.DBM.DBM import DBM
from models.Logger.Logger import Logger


class SpiderHandler(object):
    def __init__(self, handler=None):
        self._handler = handler

    def handle(self, params):
        Logger().info("prcessing....%s" % type(self))
        processed = self.process(params)
        if processed['res'] is None:
            if self._handler is not None:
                processed = self._handler.handle(params)
        self.diff(params, processed)

    @abstractmethod
    def process(self, params):
        pass

    def diff(self, params, processed):
        if processed is not None and processed['res'] is not None:
            dbm = DBM()
            # diff rank
            md5 = hashlib.md5()
            # handlder + keyword
            md5.update(params + '.' + type(self).__name__)
            key = md5.hexdigest()
            previous_rank = dbm.get(key)
            if previous_rank is None:
                dbm.set(key, processed['rank'])
            else:
                previous_rank = int(previous_rank)
                current_rank = int(processed['rank'])

                if previous_rank > current_rank:
                    Logger().info('rank has inecreased!send notify to others')
                    dbm.set(key, current_rank)

                elif previous_rank < current_rank:
                    Logger().info('rank has decreased!send notify to others')
                    dbm.set(key, current_rank)
                else:
                    Logger().info('rank has not changed,don`t need to disturb others')

        else:
            if self._handler is None:
                # last one handler is none , notify admin users
                Logger().cri('last one handler:%s' % type(self))
                Logger().cri('very bad, need to alert the developers!')
