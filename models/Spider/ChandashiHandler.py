#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import HTMLParser
import re
from models.Config.Config import Config
from models.Spider.SpiderHandler import SpiderHandler
from pyquery import PyQuery


class ChandashiHandler(SpiderHandler):
    URL = 'https://www.chandashi.com/search/index.html?keyword=%s&type=store&view=web'

    def __init__(self, handler=None):
        super(ChandashiHandler, self).__init__(handler)

    def process(self, params):

        print 'processing...%s' % type(self)

        url = self.URL % params

        rank = None
        response = None
        request = urllib2.Request(url, None, Config.HEADERS)
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            if hasattr(e, 'code'):
                rank = None
        finally:
            if response:
                if re.match(ur'.*' + params + '.*', response.geturl()):
                    """前后url比较"""
                    appname = Config.parse_config('app', 'appname')
                    doc = PyQuery(HTMLParser.HTMLParser().unescape(response.read()))
                    apps = doc('.searchlist .limit')
                    for app in apps.items():
                        group = re.search(ur'(\d+)\s:\s' + appname + '', app.text())
                        if group:
                            rank = group.group(1)
        if rank is not None:
            return int(rank)
        else:
            return None
