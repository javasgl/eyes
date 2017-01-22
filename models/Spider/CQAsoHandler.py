#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.Spider.SpiderHandler import SpiderHandler


class CQAsoHandler(SpiderHandler):
    def __init__(self, handler=None):
        super(CQAsoHandler, self).__init__(handler)

    def process(self, params):
        print 'cqaso%s' % params
        return None
