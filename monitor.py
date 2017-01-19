#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from models.spider import *
from models.config import *


@click.group()
def start():
    """This is AppRankMonitor Tool"""

    pass


@start.command()
@click.option('--keyword', default='appname', help='search keyword to be watched!')
def run(keyword):
    """start to run"""
    print keyword

    pass


@start.command()
def getconfig():
    """view config files"""
    for mail in Config.parse_config('admin', 'mailList').split(','):
        print mail
    spider = Spider.get_intance()
    print spider.set_url('https://baidu.com').parse()


@start.command()
@click.option('--date', help='eg:2016-12-29')
def getlog(date):
    """view log files"""
    print date
    print 'log'
