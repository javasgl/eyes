#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from models.Logger.Logger import Logger


class LogView(object):
    def __init__(self):
        self._date = ''
        self._line = 0

    def set_date(self, date):
        self._date = date
        return self

    def set_count(self, line):
        self._line = line
        return self

    def view_log(self):
        if time.mktime(time.strptime(self._date, '%Y-%m-%d')) > time.time():
            print '--date cant`t be bigger then today!'
        else:
            if self._line > 50:
                print 'may be --line is too huge?!'
            else:
                logfile = Logger.get_log_file(self._date)
                if os.path.exists(logfile) and os.path.isfile(logfile) and os.access(logfile, os.R_OK):
                    os.system('tail -%d %s' % (self._line, logfile))
                else:
                    print 'log file is not exists or can`t be readable! please check the config [log] section and the system permission'
            pass
