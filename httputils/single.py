#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/8/16 3:55 PM
# @Author  : YangGao
# @File    : single.py

from queue import Queue
from threading import Thread
from httputils.downlaod import *


class DownloadWorker(Thread):
    def __init__(self, my_q, name):
        Thread.__init__(self)
        self.queue = my_q
        self.name = name

    def run(self):
        while True:
            # print('coming' + self.name)
            # Get the work from the queue and expand the tuple
            # 特别注意 方法带括号和不带括号的区别 带()直接返回值 不带()返回地址 有地址为真，无地址为假
            if not self.queue.empty():
                # directory, link = self.queue.get()
                # download_link(directory, link)
                # tells the queue that the processing
                # on the task is complete.
                print(self.queue.get() + '--->' + self.name)
                self.queue.task_done()
                # else:
                #     print('done' + self.name)


def main():
    # ts = time.time()
    counter = 0
    # client_id = os.getenv('IMGUR_CLIENT_ID')
    # if not client_id:
    #     raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    # download_dir = setup_download_dir()
    # links = [l for l in get_links(client_id) if l.endswith('.jpg')]
    test_links = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    test_name = ['Thread-1', 'Thread-2', 'Thread-3', 'Thread-4']
    # Create a queue to communicate with the worker threads
    my_queue = Queue()
    # Create 8 worker threads
    for x in test_name:
        worker = DownloadWorker(my_queue, x)
        # Setting daemon(守护进程) to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        print('-----Thread start :' + str(counter))
        counter += 1
        worker.start()
    # Put the tasks into the queue as a tuple
    for link in test_links:
        logger.info('Queueing {}'.format(link))
        print('start fill the queue ==  ' + link)
        my_queue.put(link)
        # queue.put((download_dir, link))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    my_queue.join()
    # print('Took {}'.format(time.time() - ts))
    print('main end')


main()
#
# from functools import partial
# from multiprocessing.pool import Pool
#
#
# def multiple_processes():
#     ts = time()
#     client_id = os.getenv('IMGUR_CLIENT_ID')
#     if not client_id:
#         raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
#     download_dir = setup_download_dir()
#     links = [l for l in get_links(client_id) if l.endswith('.jpg')]
#     download = partial(download_link, download_dir)
#     with Pool(8) as p:
#         p.map(download, links)
#     print('Took {}s'.format(time() - ts))
