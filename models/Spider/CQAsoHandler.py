#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import json
from models.Config.Config import Config
from models.Spider.SpiderHandler import SpiderHandler


class CQAsoHandler(SpiderHandler):
    URL = 'http://backend.cqaso.com/search/%s?sortBy=nature&limit=20&offset=0&country=CN'

    def __init__(self, handler=None):
        super(CQAsoHandler, self).__init__(handler)

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
                    result = json.loads(response.read(), encoding="utf-8")
                    for app in result['contents']:
                        group = re.search(ur'^' + appname + '', app['name'])
                        if group:
                            rank = app['nowRank']

        if rank is not None:
            return int(rank)
        else:
            return None
