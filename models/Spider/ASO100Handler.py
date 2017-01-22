#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
from models.Config.Config import Config
from models.Logger.Logger import Logger
from models.Spider.SpiderHandler import SpiderHandler
from pyquery import PyQuery


class ASO100Handler(SpiderHandler):
    URL = 'https://aso100.com/search?country=cn&search=%s'
    REGEX = '.*<h4 class="media-heading"><a.*>(\d+)、%s.*<\/a><\/h4>.*'

    def __init__(self, handler=None):
        super(ASO100Handler, self).__init__(handler)

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
                print 'Error:', e.code, e.reason
        finally:
            if response:
                if re.match(ur'.*' + params + '.*', response.geturl()):
                    """前后url比较"""
                    appname = Config.parse_config('app', 'appname')
                    doc = PyQuery(response.geturl())
                    apps = doc('.media-heading')
                    for app in apps.items():
                        group = re.search(ur'(\d+)、' + appname + '', app.text())
                        if group:
                            rank = group.group(1)

                else:
                    print 'res:%s,%s' % (response.geturl(), type(self))
                    print 'url:%s,%s' % (url, type(self))
                    print 'redirected!need alert'
        if rank is not None:
            print rank
        else:
            return None
