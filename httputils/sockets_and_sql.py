#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/11/16 9:18 AM
# @Author  : YangGao
# @File    : sockets_and_sql.py

import socket
# import sys
from _thread import *

#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# print(s)

# server_name = 'pythonprogramming.net'

# port = 80
# 104.237.143.20
# server_ip = socket.gethostbyname(server_name)
# print(server_ip)

#
# request = 'GET/HTTP/1.1\nHost: ' + server_name + '\n\n'
# s.connect((server_name, port))
# s.send(request.encode())
# # response = s.recv(4049)
# # print(response)
#
# response = s.recv(32)
#
# while len(response) > 0:
#     print(response)
#     response = s.recv(32)

# def pscan(port):
#     try:
#         # 特别注意 函数参数 是一个 tuple
#         s.connect((server_name, port))
#         return True
#     except:
#         return False
#
# # range 区间是 从 包含 1 到包含 25 -->【1，26）
# for x in range(1, 26):
#     if pscan(x):
#         print('port ', x, 'is open')
#     else:
#         print('port ', x, 'is closed')
# # 当上面 运行完后 端口 关闭后 下面的是 80 也是关闭的
# if pscan(80):
#     print('port ', '80', 'is open')
# else:
#     print('port is closed')

# import threading
# from queue import Queue
#
# print_lock = threading.Lock()
#
#
# def port_scan(port):
#     try:
#         # make sure codes print task started by one thread at time
#         con = s.connect((server_name, port))
#         with print_lock:
#             print('port ', port)
#             print(port, 'open ')
#         # print(port, 'open ')
#         # 会触发except
#         con.close()
#     except:
#         print(port, ' closed ')
#
#
# def threader():
#     while 1:
#         print('while loop')
#         # 当 q 没有队列时 将有 q.join结束线程
#         try:
#             worker = q.get()
#             print('get', worker)
#             port_scan(worker)
#             print('task_done', worker)
#             q.task_done()
#         except:
#             print('get nothing')
#
#
# q = Queue()
# # make 10 threads
# for x in range(3):
#     t = threading.Thread(target=threader)
#     t.daemon = True
#     t.start()
#
# for worker in range(1, 10):
#     print('put worker===>', str(worker))
#     q.put(worker)
#
# q.join()
# print('main is shut down')


# ================================================================================
# host = ''
# port = 5555
#
# try:
#     s.bind((host, port))
# except socket.error as e:
#     print('bind error :' + str(e))
#
# s.listen(5)


# conn, addr = s.accept()
#
# print('connected to : ' + addr[0] + ':' + str(addr[1]))

#
# def threaded_client(conn):
#     conn.send(str.encode('welcome,type your name'))
#     while 1:
#         print(' data waiting ======')
#         # 等待有阻塞功能
#         data = conn.recv(2048)
#         if not data:
#             print('conn has destroyed')
#             break
#         print(' data coming')
#         reply = 'server output : ' + data.decode('utf-8')
#         print(reply)
#
#         conn.sendall(str.encode(reply))
#     conn.close()

#
# while 1:
#     print('while loop start conn=======>>')
#     #  会阻塞 直到建立起链接 ，第二次 进来 阻塞了 是因为 第一次已经 被建立了，
#     # 导致这次没有和其他 建立链接，所以在主线程里print 不会被继续运行下去。
#     conn, addr = s.accept()
#     print('connected to : ' + addr[0] + ':' + str(addr[1]))
#     start_new_thread(threaded_client, (conn,))

'''
johnsdeMacBook-Pro:~ johnsmac$ telnet 192.168.0.101 5555
Trying 192.168.0.101...
Connected to 192.168.0.101.
Escape character is '^]'.
Connection closed by foreign host.
'''
# print('while loop start conn=======>>')
# conn, addr = s.accept()
# if conn:
#     print('conn does work now')
# else:
#     print('conn does not work yet')
# print('connected')
# start_new_thread(threaded_client, (conn,))
# # 需要再次连接，为何需要再次连接？？？因为 起的是线程 ，
# # 函数 会 直接 运行完毕 退出 ，导致端口关闭，线程的代码还没来得及运行
# # conn, addr = s.accept()
# # print(' this will never be printed')
# ----------------------------------------------------------------------------------------

# socketpair()创建一对连接socket，用于父子进程间的通信。

# import os
#
# parent, child = socket.socketpair()
#
# pid = os.fork()
#
# if pid:
#     print('in parent, sending message')
#
#     child.close()
#     parent.sendall('ping')
#     response = parent.recv(1024)
#     print('response from child:', response)
#
#     parent.close()
#
# else:
#     print('in child, waiting for message')
#
#     parent.close()
#     message = child.recv(1024)
#     print('message from parent:', message)
#
#     child.sendall('pong')
#     child.close()


# =======================SQL==============================

# import sqlite3
# import time
# import datetime
# import random

'''
If given database name does not exist then
this call will create the database. You can
specify filename with required path as well
if you want to create database anywhere else
except in current directory.
but now we wanna create it in current directory
'''
# conn = sqlite3.connect('base.db')
# c = conn.cursor()

# def create_table():
#     c.execute(
#         'CREATE TABLE IF NOT EXISTS STUFF (unix REAL, dateStamp TEXT, keyword TEXT ,value REAL)')
#
#
# def data_insert():
#     c.execute('INSERT INTO STUFF VALUES(13222,"2016-11-14","python",5)')
#     conn.commit()
#     c.close()
#     conn.close()
#
#
# def dynamic_data_entry():
#     unix = time.time()
#     date_stamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m_%d %h:%M:%S'))
#     keyword = 'Python'
#     value = random.randrange(0, 10)
#     c.execute('INSERT INTO STUFF (unix, dateStamp,keyword,value)VALUES (?,?,?,?)', (unix, date_stamp, keyword, value))
#     conn.commit()
#     '''sqlite3.ProgrammingError: Cannot operate on a closed database.'''
#     # conn.close()
#

# def crate_table_stock():
#     # Create table
#     c.execute('''CREATE TABLE stocks
#                  (date TEXT, trans TEXT, symbol TEXT, qty REAL, price REAL)''')
#
#     # Insert a row of data
#     c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
#     # Save (commit) the changes
#     conn.commit()
#
#     # We can also close the connection if we are done with it.
#     # Just be sure any changes have been committed or they will be lost.
#     conn.close()


# def query_stock():
#     # Never do this -- insecure!
#     # symbol = 'RHAT'
#     # c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
#
#     # Do this instead
#     t = ('RHAT',)
#     c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#     print
#     c.fetchone()
#
#     # Larger example that inserts many records at a time
#     purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#                  ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#                  ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#                  ]
#     c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


# def read_from_db():
#     sql_str = 'select * from STUFF where value=3 and  keyword="Python"'
#     c.execute(sql_str)
#     # data = c.fetchall()
#     # print(data)
#     for row in c.fetchall():
#         print(row)


# =======================================================
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from matplotlib import style
#
# style.use('fivethirtyeight')


# def graph_data():
#     sql_command = 'select unix, value from STUFF'
#     data = c.execute(sql_command).fetchall()
#     dates = []
#     values = []
#     for row in data:
#         dates.append(datetime.datetime.fromtimestamp(row[0]))
#         values.append(row[1])
#         # print(row[0])
#         # print(datetime.datetime.fromtimestamp(row[0]))
#     '''
#     now here is dates : ===>
#         [(1479093511.86433, 3.0),
#          (1479093512.869195, 0.0),
#          (1479093513.876131, 7.0),
#          (1479093514.880354, 1.0),
#          (1479093515.88761, 2.0),
#          (1479093516.895772, 3.0),
#          (1479093517.900329, 1.0),
#          (1479093518.90731, 6.0),
#          (1479093519.912231, 6.0),
#          (1479093520.919072, 1.0)]
#    '''
#     # print('now here is dates : ===> \n', dates)
#     plt.plot_date(dates, values, '-')
#     plt.show()

#
# def del_and_update():
#     # sql_command = 'select * from STUFF'
#     # c.execute(sql_command)
#     # [print(row) for row in c.fetchall()]
#     # print(50*'==')
#     # sql_update_command = 'update STUFF set value = 99 where VALUE =3'
#     # c.execute(sql_update_command)
#     # conn.commit()
#     # c.execute(sql_command)
#     # [print(row) for row in c.fetchall()]
#     # c.execute('DELETE FROM STUFF where value=3')
#     # conn.commit()
#

# del_and_update()
# graph_data()
# ==console==============================================
# read_from_db()
# create_table()
# data_insert()

# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)
# c.close()
# conn.close()
