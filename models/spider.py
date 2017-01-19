#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, re


class Spider(object):
    """docstring for Spider"""

    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
        'Referer': ''
    }

    def __init__(self):
        self._url = ''
        self._keyword = ''
        self._regexp = ''

    @staticmethod
    def get_intance():
        return Spider()

    def set_url(self, url):
        self._url = url
        return self

    def set_keyword(self, keyword):
        self._keyword = keyword
        return self

    def set_regexp(self, regexp):
        self._regexp = regexp
        return self

    def parse(self):

        self._url = 'http://aso100.com/search?country=cn&search=%s' % self._keyword
        response = None
        request = urllib2.Request(self._url, None, Spider.HEADERS)
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            if hasattr(e, 'code'):
                print 'Error:', e.code, e.reason
        finally:
            if response:
                if re.match(r'.*appname.*', response.geturl()):
                    """https http比较"""
                    print 'no redirect'

                    group = re.search(self._regexp, response.read())
                    if group:
                        print 'matched'
                        print group.group(1)
                        return response.read()
                    else:
                        print 'not matched'
                else:
                    # print response.read()
                    print response.geturl()
                    print self._url
                    print 'redirected!need alert'
