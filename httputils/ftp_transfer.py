#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/10/16 4:26 PM
# @Author  : YangGao
# @File    : ftp_transfer.py
from ftplib import FTP

ftp = FTP('')
ftp.login(user='username', passwd='password')
ftp.cwd('/specificdomain-or-location/')


def grab_file():
    file_name = 'fileName.txt'
    local_file = open(file_name, 'wb')
    ftp.retrbinary('RETR ' + file_name, local_file.write, 1024)
    ftp.quit()
    local_file.close()


def place_file():
    file_name = 'fileName.txt'
    ftp.storbinary('STOR' + file_name, open(file_name, 'rb'))
    ftp.quit()
