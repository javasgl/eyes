#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.Spider.SpiderHandler import SpiderHandler


class ChandashiHandler(SpiderHandler):
    def __init__(self, handler=None):
        super(ChandashiHandler, self).__init__(handler)

    def process(self, params):
        return None
