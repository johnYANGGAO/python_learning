#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/10/16 3:02 PM
# @Author  : YangGao

import sys
'''
johnsdeMacBook-Pro:~ johnsmac$ python
Python 2.7.10 (default, Jul 30 2016, 18:31:42)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import subprocess
>>> subprocess.call('ls',shell=True)
Applications			johnsonyanggaogithub
Desktop				johnsonyanggaogithub.pub
Documents			private.key
Downloads			public.key
Library				public_key.der
Movies				python-evn
Music				selfsign.crt
Pictures			selfsign.csr
Public				selfsign.key
0
>>> subprocess.call('python /Users/johnsmac/Desktop/test_setup.py "this is from out "', shell=True)
['/Users/johnsmac/Desktop/test_setup.py', 'this is from out ']
0
>>>

'''
print(sys.argv)
