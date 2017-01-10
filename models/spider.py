class Spider(object):
    """docstring for Spider"""

    def __init__(self):
        self._url = ''

    def parse(self):
        return 'Spider parse...url:%s' % self._url

    @staticmethod
    def get_intance():
        return Spider()

    def set_url(self, url):
        self._url = url
        return self
