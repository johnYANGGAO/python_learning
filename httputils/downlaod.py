#!/usr/bin/env python
# coding=utf-8

import json
import logging
import os
# import time
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)
test_url = 'https://s-media-cache-ak0.pinimg.com/originals/64/32/57/643257288ac866dc829b41cca1b6d051.jpg'
base_url = ''
'''{
   "data":
      {"error":"Authentication required",
      "request":"\/3\/gallery\/",
      "method":"GET"
      },
   "success":false,
   "status":401
   }'''


def get_links(client_id):
    headers = {'Authorization': 'Client-ID{}'.format(client_id)}
    req = Request(base_url, headers=headers, method='GET')
    with urlopen(req) as resp:
        data = json.loads(resp.readall().decode('utf-8'))
    return map(lambda item: item['link'], data['data'])


def download_link(directory, link):
    logger.info('Downloading %s', link)
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as file:
        file.write(image.readall())


def setup_download_dir():
    download_dir = Path('/Users/johnsmac/Documents/my_git_center/py_project_fun_center/images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir

#
# def main():
#     ts = time.time()
#     client_id = os.getenv('IMGUR_CLIENT_ID')
#     if not client_id:
#         raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
#     download_dir = setup_download_dir()
#     links = [l for l in get_links(client_id) if l.endswith('.jpg')]
#     for link in links:
#         download_link(download_dir, link)
#     print('Took {}s'.format(time() - ts))

#
# def download_img_test():
#     # 1 Request first
#     # 2 link net using Request object then get response object
#     # 3  whatever given using Response read fuc
#
#     req = Request(test_url, method='GET')
#     resp = urlopen(req)
#     response_data = resp.read()
#     file_path = setup_download_dir() / os.path.basename('test.jpg')
#     # print(respData)
#     # 特别注意 对 对象的方法使用 ，虽然 分配对象时无需 列出 类，但一定要分清
#     file = file_path.open('wb')
#     file.write(response_data)
#     print('down')
#

# download_img_test()






