#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SpiderHandler


class ASO100Handler(SpiderHandler.SpiderHandler):
    def __init__(self, handler=None):
        SpiderHandler.SpiderHandler.__init__(self, handler)

    def process(self, params):
        return None
