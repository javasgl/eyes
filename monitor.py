#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sys
import hashlib

from models.Config.Config import Config
from models.Logger.Logger import Logger
from models.Spider.ChandashiHandler import ChandashiHandler
from models.Spider.ASO100Handler import ASO100Handler
from models.Spider.CQAsoHandler import CQAsoHandler


@click.group()
def start():
    """This is AppRankMonitor Tool"""
    reload(sys)
    sys.setdefaultencoding('utf-8')
    pass


@start.command()
@click.option('--keyword', default='appname', help='search keyword to be watched!')
def run(keyword):
    """start to run"""
    Logger().debuger('keyword:%s' % keyword)
    ChandashiHandler(ASO100Handler(CQAsoHandler())).handle(keyword)

    pass


@start.command()
def getconfig():
    """view config files"""
    for mail in Config.parse_config('admin', 'mailList').split(','):
        print mail


@start.command()
@click.option('--date', help='eg:2016-12-29')
def getlog(date):
    """view log files"""
    print date
    print 'log'
