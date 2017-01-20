#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod


class SpiderHandler(object):
    def __init__(self, handler=None):
        self._handler = handler

    def handle(self, params):
        processed = self.process(params)
        if processed is None:
            if self._handler is not None:
                processed = self._handler.handle(params)
        else:
            print processed
            print 'success'
        return processed

    @abstractmethod
    def process(self, params):
        pass
