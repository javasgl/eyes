#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser


class Config(object):
    CONFIG_FILE = 'config/config.ini'

    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
        'Referer': ''
    }

    def __init__(self):
        pass

    @staticmethod
    def parse_config(section, key):
        config = ConfigParser.ConfigParser()
        config.read(Config.CONFIG_FILE)
        return config.get(section, key)
