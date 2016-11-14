#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/5/16 6:55 PM
# @Author  : YangGao
# @Site    : 
# @File    : __init__.py.py

import _md5


def md5sum(t):
    return _md5.md5(t).hexdigest()

'''TypeError: Unicode-objects must be encoded before hashing'''
print(md5sum(str.encode('高杨')))
