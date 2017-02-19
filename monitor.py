#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sys
import time

from models.Logger.LogView import LogView
from models.Config.Config import Config
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
    CQAsoHandler(ChandashiHandler(ASO100Handler())).handle(keyword)
    pass


@start.command()
def getconfig():
    """view config files"""
    for mail in Config.parse_config('admin', 'mailList').split(','):
        print mail


@start.command()
@click.option('--date', default=time.strftime('%Y-%m-%d'), help='eg:--date=2016-12-29')
@click.option('--line', default=10, help='eg:--line=5')
def getlog(date, line):
    """view log files"""
    LogView().set_count(line).set_date(date).view_log()
