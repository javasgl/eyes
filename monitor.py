#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from models.config import *

from models.Spider.ChandashiHandler import ChandashiHandler
from models.Spider.ASO100Handler import ASO100Handler
from models.Spider.CQAsoHandler import CQAsoHandler
from models.Logger.Logger import Logger


@click.group()
def start():
    """This is AppRankMonitor Tool"""

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
