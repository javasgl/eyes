#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
from models.Config.Config import Config
from models.Logger.Logger import Logger
from models.Spider.SpiderHandler import SpiderHandler


class ASO100Handler(SpiderHandler):
    URL = 'https://aso100.com/search?country=cn&search=%s'
    REGEX = '.*<h4 class="media-heading"><a.*>(\d+)、%s.*<\/a><\/h4>.*'

    def __init__(self, handler=None):
        super(ASO100Handler, self).__init__(handler)

    def process(self, params):

        print 'processing...%s' % type(self)

        url = self.URL % params
        regex = self.REGEX % params
        response = None
        request = urllib2.Request(url, None, Config.HEADERS)
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            if hasattr(e, 'code'):
                print 'Error:', e.code, e.reason
        finally:
            if response:
                if re.match(r'.*' + params + '.*', response.geturl()):
                    """前后url比较"""

                    print 'not directed %s' % regex

                    group = re.search(r'' + regex + '', response.read())
                    if group:
                        print 'matched %s' % group.group(1)
                        return response.read()
                    else:
                        print 'not matched %s'

                else:
                    print 'res:%s,%s' % (response.geturl(), type(self))
                    print 'url:%s,%s' % (url, type(self))
                    print 'redirected!need alert'
        return 'aa'
