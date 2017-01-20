#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from models.spider import *
from models.config import *
from models.SpiderHandler import SpiderHandler
from models.ChandashiHandler import ChandashiHandler
from models.ASO100Handler import ASO100Handler
from models.CQAsoHandler import CQAsoHandler


@click.group()
def start():
    """This is AppRankMonitor Tool"""

    pass


@start.command()
@click.option('--keyword', default='appname', help='search keyword to be watched!')
def run(keyword):
    """start to run"""
    print keyword

    ChandashiHandler(ASO100Handler(CQAsoHandler())).handle(keyword)

    # Spider.get_intance().set_url('').set_keyword(keyword).set_regexp(r'.*<h4 class="media-heading"><a.*>(\d+)、appname.*<\/a><\/h4>.*').parse()
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
