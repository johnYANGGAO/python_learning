#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/10/16 9:17 AM
# @Author  : YangGao
# @File    : cx_freeze.py

from cx_Freeze import setup, Executable

'''
make exe file
'''
setup(name='urlParse', version='0.1',
      description='Parse stuff',
      executables=[Executable('/Users/johnsmac/Documents/my_git_center/py/httputils/parsing_websites.py')])
