#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time


class Logger(object):
    def __init__(self, clevel=logging.DEBUG, flevel=logging.INFO):
        # path = 'logs/%s.log' % time.strftime('%Y-%m-%d')
        path = 'logs/log.log'
        self.logger = logging.getLogger(path)
        self.logger.setLevel(clevel)

        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(clevel)
        streamhandler.setFormatter(fmt)

        filehandler = logging.FileHandler(path)
        filehandler.setLevel(flevel)
        filehandler.setFormatter(fmt)

        self.logger.addHandler(streamhandler)
        self.logger.addHandler(filehandler)

    def debuger(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)
