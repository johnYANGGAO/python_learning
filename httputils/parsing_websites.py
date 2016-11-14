#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/9/16 2:23 PM
# @Author  : YangGao
# @File    : parsing_websites.py

import urllib.request
import re
import urllib.parse

# url = 'http://pythonprogramming.net'
# json_value = {'s': 'basics', 'submit': 'search'}
#
# parameters = urllib.parse.urlencode(json_value).encode('utf-8')
#
# req = urllib.request.Request(url, parameters)
# response = urllib.request.urlopen(req)
#
# data = response.read()
#
# # print(data)
#
# paragraphs = re.findall(r'<p>(.*?)</p>', str(data))
#
# for each_item in paragraphs:
#     print(each_item)
