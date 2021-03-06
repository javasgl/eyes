#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
import os
from models.Config.Config import Config


class Logger(object):
    def __init__(self):
        path = self.get_log_file()
        self.logger = logging.getLogger(path)

        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # stream handler
        self._streamhandler = logging.StreamHandler()
        self._streamhandler.setFormatter(fmt)

        # file handler
        self._filehandler = logging.FileHandler(path)
        self._filehandler.setFormatter(fmt)

    @staticmethod
    def get_log_file(filename=time.strftime('%Y-%m-%d')):
        if os.path.exists(Config.parse_config('log', 'logdir')):
            return '%s%s.log' % (Config.parse_config('log', 'logdir'), filename)
        else:
            raise OSError("config dir is not exists")

    def debuger(self, message):
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self._streamhandler)
        self.logger.debug(message)

    def info(self, message):
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self._filehandler)
        self.logger.info(message)

    def error(self, message):
        self.logger.setLevel(logging.ERROR)
        self.logger.addHandler(self._streamhandler)
        self.logger.addHandler(self._filehandler)
        self.logger.error(message)

    def cri(self, message):
        self.logger.setLevel(logging.CRITICAL)
        self.logger.addHandler(self._streamhandler)
        self.logger.addHandler(self._filehandler)
        self.logger.critical(message)

    def __del__(self):
        self.logger.removeHandler(self._filehandler)
        self.logger.removeHandler(self._streamhandler)
