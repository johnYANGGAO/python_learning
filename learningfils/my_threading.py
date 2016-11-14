#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/9/16 4:43 PM
# @Author  : YangGao
# @File    : my_threading.py
# 特别注意：文件名称 非继承 不能 和 API 的一致 否则视为覆盖
import threading
import time
from queue import Queue

#
# exitFlag = 0
#
#
# class MyThread(threading.Thread):
#     def __init__(self, thread_id, name, delay):
#         threading.Thread.__init__(self)
#         self.threadID = thread_id
#         self.name = name
#         self.delay = delay
#
#     def run(self):
#         print("Starting " + self.name)
# Get lock to synchronize threads
#         threadLock.acquire()
#         print_time(self.name, self.delay, 5)
#         print("Exiting " + self.name)
# Free lock to release next thread
#         threadLock.release()


#
#
# def print_time(thread_name, delay, counter):
#     while counter:
#
#         if exitFlag:
#             thread_name.exit()
#
#         time.sleep(delay)
#
#         print("%s: %s" % (thread_name, time.ctime(time.time())))
#
#         counter -= 1
#
#
# # Create new threads
# thread1 = MyThread(1, "Thread-1", 1)
# thread2 = MyThread(2, "Thread-2", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
#
# print('down')

#
# import queue
# import threading
# import time
#
# q_line = queue.Queue(5)
#
# exitFlag = 0
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# sourceList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# threads = []
# threadID = 1
#
#
# class TestThread(threading.Thread):
#     def __init__(self, thread_id, name, line):
#         threading.Thread.__init__(self)
#         self.threadID = thread_id
#         self.name = name
#         self.q = line
#
#     def run(self):
#         print("Starting " + self.name)
#         process_data(self.name, self.q)
#         print("Exiting " + self.name)
#
#
# def process_data(thread_name, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not q.empty():
#             data = q.get()
#             print("%s processing %s" % (thread_name, data))
#             queueLock.release()
#         else:
#             queueLock.release()
#         time.sleep(1)
#         print(thread_name + '---exitFlag :' + str(exitFlag))
#
#
# # Fill the queue
# queueLock.acquire()
# for word in sourceList:
#     q_line.put(word)
# queueLock.release()
#
# # Create new threads
# for tName in threadList:
#     thread = TestThread(threadID, tName, q_line)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
#
# # Wait for queue to empty
'''the pass statement does nothing particular
 but can act as a placeholder, as shown before. 'cause
 Python has the syntactical requirement
 that code blocks (after if, except, def, class etc.)
  cannot be empty'''
# while not q_line.empty():
#     pass
#
# # Notify threads it's time to exit
# exitFlag = 1
#
''' join() It's like wait_until_finished(some_thread).'''
# # Wait for all threads to complete
# for t in threads:
#     t.join()
# print("Exiting Main Thread")

print_lock = threading.Lock()
q = Queue()


def do_work(issue):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name, issue)


'''
true loop -->1
true loop -->2
true loop -->3
true loop -->4
true loop -->5
loaded -->0
loaded -->1
loaded -->2
loaded -->3
loaded -->4
loaded -->5
loaded -->6
loaded -->7
loaded -->8
loaded -->9
loaded -->10
loaded -->11
loaded -->12
loaded -->13
loaded -->14
loaded -->15
loaded -->16
loaded -->17
loaded -->18
loaded -->19
Thread-2 3
通知 ：3
true loop -->6
Thread-3 2
通知 ：2
true loop -->7
Thread-4 1
通知 ：1
true loop -->8
Thread-1 0
通知 ：0
true loop -->9
Thread-5 4
通知 ：4
true loop -->10
Thread-2 5
通知 ：5
true loop -->11
Thread-4 6
通知 ：6
true loop -->12
Thread-3 7
通知 ：7
true loop -->13
Thread-1 8
通知 ：8
true loop -->14
Thread-5 9
通知 ：9
true loop -->15
Thread-2 10
通知 ：10
true loop -->16
Thread-1 13
通知 ：13
true loop -->17
Thread-4 11
通知 ：11
true loop -->18
Thread-3 12
通知 ：12
true loop -->19
Thread-5 14
通知 ：14
true loop -->20
Thread-2 15
通知 ：15
true loop -->21
Thread-4 17
通知 ：17
true loop -->22
Thread-1 16
通知 ：16
true loop -->23
Thread-3 18
通知 ：18
true loop -->24
Thread-5 19
通知 ：19
true loop -->25
ok ,main now  2.018125057220459

'''

counter = 0


def threader():

    global counter
    # 当取完queue 里的数据时 loop 将停止？
    while True:
        counter += 1
        print('true loop -->' + str(counter))
        employee = q.get()
        do_work(employee)
        # 因为有了join等待，所以完成一个就通知一个
        print('通知 ：' + str(employee))
        q.task_done()


for x in range(5):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)
    print('loaded -->' + str(worker))

q.join()

print('ok ,main now ', time.time() - start)
