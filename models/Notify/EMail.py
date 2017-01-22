#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import smtplib
import mimetypes
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from models.Config.Config import Config


class EMail(object):
    """
        example:
            EMail().set_from('monitor', 'who@doamin') \
            .set_to('who<who@doamin>') \
            .set_subject('title') \
            .set_content('<a href="http://www.qq.com">this is content</a>') \
            .set_append_content('this is addon content')\
            .set_mimetype('html') \
            .set_recevers('who1@doamin') \
            .set_recevers('who2@doamin') \
            .set_attachment('logs/log.log') \
            .set_attachment('logs/cat12.gif') \
            .send()
    """
    def __init__(self):
        self._mail_host = Config.parse_config('email', 'host')
        self._mail_user = Config.parse_config('email', 'user')
        self._mail_passwd = Config.parse_config('email', 'passwd')
        self._sender = ''
        self._receviers = []
        self._from = ''
        self._to = ''
        self._content_type = 'plain'
        self._content = ''
        self._subject = ''
        self._attachments = []

    def set_recevers(self, recevier):
        self._receviers.append(recevier)
        return self

    def set_from(self, fromstr, _sender):
        self._sender = _sender
        self._from = '%s<%s>' % (Header(fromstr, 'utf-8'), self._sender)
        return self

    def set_to(self, tostr):
        self._to = Header(tostr, 'utf-8')
        return self

    def set_mimetype(self, content_type='plain'):
        self._content_type = content_type
        return self

    def set_content(self, content):
        if not isinstance(content, unicode):
            content = unicode(content, 'utf-8')
        self._content = content
        return self

    def set_subject(self, subject):
        if not isinstance(subject, unicode):
            subject = unicode(subject, 'utf-8')
        self._subject = subject
        return self

    def set_attachment(self, filename):
        self._attachments.append(filename)
        return self

    def set_append_content(self, append=''):
        if append is not None:
            self._content = '%s(%s)' % (self._content, append)

    def send(self):
        if self._content is None:
            raise Exception('email content must not be empty!')

        message = MIMEMultipart()

        if self._content_type is 'html':
            message.attach(MIMEText(self._content, 'html', 'utf-8'))
        else:
            message.attach(MIMEText(self._content, 'plain', 'utf-8'))

        message['Date'] = time.strftime('%Y-%m-%d %H-%M-%S')
        message["Accept-Language"] = "zh-CN"
        message["Accept-Charset"] = "ISO-8859-1,utf-8"

        message["Subject"] = self._subject
        message["From"] = self._from
        message["To"] = self._to

        for filename in self._attachments:
            if filename is not None and os.path.exists(filename):
                ctype, encoding = mimetypes.guess_type(filename)
                if ctype is None or encoding is not None:
                    ctype = "application/octet-stream"
                attachmentname = os.path.split(filename)[1]
                maintype, subtype = ctype.split("/", 1)
                attachment = MIMEImage((lambda f: (f.read(), f.close()))(open(filename, "rb"))[0], _subtype=subtype)
                attachment.add_header("Content-Disposition", "attachment", filename=attachmentname)
                message.attach(attachment)
        smtp = smtplib.SMTP()
        smtp.connect(self._mail_host)
        smtp.login(self._mail_user, self._mail_passwd)
        smtp.sendmail(self._sender, self._receviers, message.as_string())
        smtp.quit()
