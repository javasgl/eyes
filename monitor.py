import sys, os
import click
import ConfigParser
from models.spider import *
from models.config import *


@click.group()
def start():
    """This is AppRankMonitor Tool"""
    pass


@start.command()
def getconfig():
    """view config files"""
    config = ConfigParser.ConfigParser()
    filepath = './config/config.ini'
    config.read(filepath)
    s = config.sections()
    print 'get config', s
    o = config.options('mails')
    print 'get options', o
    i = config.items('mails')
    print 'get itmes', i
    print 'env:', config.get('env', 'debug')
    spider = Spider.get_intance()
    print spider.set_url('https://baidu.com').parse()


@start.command()
def getlog():
    """view log files"""
    print 'log'
