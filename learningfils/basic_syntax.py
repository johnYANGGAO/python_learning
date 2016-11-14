#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/5/16 6:56 PM
# @Author  : YangGao
# from somePackage import *  # this statement should be used sparingly(谨慎的).
# import sys
# import calendar
# import time
# import statistics as custom_s
# from statistics import variance as custom_v
# import math
# import os

# import urllib.request
# import urllib.response
# import urllib.parse
'''
codes below about api

'''
# print(sys.version)
# print('we\'re going to the store ')
# print("My name is %s and weight is %d kg!" % ('gaoyang', 68))

'''
C:\\where
C:\where
'''
# print(r'C:\\where')
# print('C:\\where')
# print('hi '+'there')
# print('hi',5)
# print('hi'+str(3))
# print(float('8.3')+3)
# print(5/2)
# print(5/34)
# val=5
# print(val)
# x,y=(1,2)
# print(x)
# print(y)
# condition=1
# while condition <10:
#     print(condition)
#     condition+=1

# while True:
#     print('doing stuff')
#     time.sleep(2)

# listval=[1,2,3,43,443,33]
# for element in listval:
#     print(element)

# for x in range(1,8):
#     print(x)

# a=2
# b=8
# c=1
# d=9
# if a < b:
#     print('a is less than b')
#
'''
if if true will never go elif ,even elif is true
'''

# if a != b:
#     print('a is not equals b ')
# elif a > c:
#     print('a is greater than c')
# else:
#     print('a is equals b')

#
# if a < b > c <d:
#     print('b is greater than a and c but less than d')

# def foo():
#     print('this is func')
#     z=3+1
#     print(z)
#
# foo()

#
# def foo_parameter(num1,num2):
#     sum=num1+num2
#     print(sum)

# foo_parameter(1,3)
# foo_parameter(num2=1,num1=3)

# def fun(a,b=4):
#     print(a,b)
#
# fun(3)
# fun(3,5)

# x=6
#
#
# def get_global():
#     print(x)
#     return 7


'''wrong'''
# def get_globalA():
#     print(x)
#     x+=2

'''correct'''

# def get_globalA():
#     global x
#     print(x)
#     x+=2
#
# x=get_global()
#
# print(x)

# class calulator:
#
#
#     def addition(x, y):
#         print(x + y)
#
#     def subtraction(x, y):
#         print(x - y)
#
#     def division(x, y):
#         print(x / y)
#
#     def multiplication(x, y):
#         print(x * y)
#
#
# calulator.multiplication(2,3)
# calulator.addition(2,3)
# calulator.division(2,3)
# calulator.subtraction(2,3)
#
# def epic():
#     print('hey ,let us go to main')
#
# if __name__== '__main__':
#      print('hey , you are in the main')

#
# x=input('what is your name :')
#
# print('hello',x)

# list_val=[3,3,3,4,7,4,32,78]
#
# e=custom_s.variance(list_val)
# print(e)
# e=custom_s.stdev(list_val)
# print(e)
#
#
# e=custom_v(list_val)
# print(e)

'''tuple collections.named tuple would be better called collections.record.'''
# x = 5, 4, 3, 2
# y = [5, 4, 3, 2, 3]
# z = ['jane', 'jessy', 'janifer', 'bob', 'alice', 'steve', 'kelly']

'tuple object does not support item assignment  x[1] = 5 makes wrong'

# def fun():
#     # x[1] = 5
#     y[1] = 6
#     print(x[1], y[1])
#
# fun()

#
# y.append(88)
# # y.insert(1,7)
# # y.remove(y[1])
#
# # print(y.index(3))
# # print(y.count(3))
# print(z)
# z.sort()
# print(z)

# multiple_list = [[[1], [2, 3, 9, 2]], [2, 8], [2, 1], [2, 8, 9, 0]]
#
# print(multiple_list[0][1][2])
#

# exDict = {'jack': [15, 'blond'], 'bob': 22, 'alice': 12, 'kevin': 17}
# print(exDict)
# print(exDict['bob'])
# print(exDict['jack'][1])

# print(max(exDict))
#
# x = 5.625
# print(math.ceil(x))
# print(math.floor(x))


# curDir = os.getcwd()
'''
/Users/johnsmac/Documents/my_git_center/py/learningfils
'''
# print(curDir)
# os.mkdir('newDir')
# time.sleep(2)
# os.rename('newDir', 'newDir2')
# time.sleep(2)
# os.rmdir('newDir')

'''
this is the stderr text
this is stdout text
['/Users/johnsmac/Documents/my_git_center/py/learningfils/basic_syntax.py']
'''

# sys.stderr.write('this is the stderr text\n')
# sys.stderr.flush()
# sys.stdout.write('this is stdout text\n')


# print(sys.argv)

'''
python /users/johnsmac/Documents/my_git_center/py/learningfils/basic_syntax.py 1

'''
# if len(sys.argv) > 1:
#     print(float(sys.argv[1]))


# def main(args):
#     print(args)

'''

 python /users/johnsmac/Documents/my_git_center/py/learningfils/basic_syntax.py 'object'
object
 this is for data transfer
'''
# main(sys.argv[1])


# x=urllib.request.urlopen('http://www.baidu.com')
# print(x.read())

# url = 'http://pythonprogramming.net'
#
# values = {'s': 'basic', 'submit': 'search'}
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
#
# request = urllib.request.Request(url, data)
# response = urllib.request.urlopen(request)
#
# responseData = response.read()
#
# print(responseData)

# try:
#     x = urllib.request.urlopen('https://www.google.com', 10000)
#     print(x.read())
# except Exception as e:
#     print(str(e))
#
# try:
#     url = 'http://www.baidu.com'
#
#     headers = {}
#     headers['User-Agent'] = 'Mozilla/5.0 '
#     req = urllib.request.Request(url, headers=headers)
#     resp = urllib.request.urlopen(req)
#     respData = resp.read()
#
#     saveFile = open('withHeader.txt', 'w')
#     saveFile.write(str(respData))
#     saveFile.close()
#
# except Exception as e:
#     print(str(e))

# cal = calendar.month(2016, 11)
# print("Here is the calendar:")
# print(cal)


'''
1478484227.480408
time.struct_time(tm_year=2016, tm_mon=11, tm_mday=7, tm_hour=2, tm_min=5, tm_sec=24, tm_wday=0, tm_yday=312, tm_isdst=0)
standard
Mon Nov  7 10:09:35 2016
'''

# ticks = time.time()
# get_time = time.gmtime()
# local_time = time.localtime()
# standard = time.asctime(time.localtime(time.time()))
# print(standard)

#
# def change(parameter):
#     parameter = [1, 2, 3, 4]
#     print('Values inside the function: ', parameter)
#     return
#
#
# my_list = [10, 20, 30]
# change(my_list)
# print('Values outside the function: ', my_list)

'''
arg1 is : 70
var in for loop :60
var in for loop :50
'''

# def print_info(arg1, *var_tuple):
#     print('arg1 is : ' + str(arg1))
#     for var in var_tuple:
#         print('var in for loop :' + str(var))
#     return

# def print_info(*var_tuple):
#     for var in var_tuple:
#         print('var in for loop :' + str(var))
#     return


# def print_info(arg1, arg2, *var_tuple):
#     print('arg1 is : ' + str(arg1) + "---" + str(arg2))
#     for var in var_tuple:
#         print('var in for loop :' + str(var))
#     return


'''
TypeError: print_info() missing 1 required positional argument: 'arg2'

'''

# print_info(10)
# print_info(70, 60, 9, 8, 50)

#
# total = 0  # This is global variable.
# name = 'hello'
#
#
# def sum_add(arg1, arg2):
#     # global total
#     # Inside the function local hello total :30
#     # Outside the function global is  30
#     total = arg1 + arg2  # Here total is local variable.
#     print("Inside the function local %s total :%d " % (name, total))
#     return total
#
#
# '''
# Inside the function local hello total :30
# Outside the function global is  0
# '''
# sum_add(10, 20)
# print("Outside the function global is ", total)
#
# class Employee:
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def display_count(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def display_employee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
#
#
# class Son(Employee):
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount -= 1
#
#     # def __init__(self):
#     #     print('this is the son of Employee')
#
#     def display_employee(self):
#         print('Name : ', self.name, ", Salary: ", self.salary)


# # son = Son()
# son = Son('brother jack', 15000)
# son.display_employee()
# son.display_count()
# # <function Employee.display_count at 0x10da5e2f0>
# print(Employee.display_count)
# Employee.display_count(son)
#
# father = Employee('big jack', 5800)
# father.display_count()
#
# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

"This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"

# emp2 = Employee("Manni", 5000)
# emp1.display_employee()
# emp2.display_employee()
# print("Total Employee %d" % Employee.empCount)
# emp1.age = 7  # Add an 'age' attribute.
# emp1.age = 8  # Modify 'age' attribute.
# del emp1.age  # Delete 'age' attribute.
# setattr(emp1, 'age', 8)  # Set attribute 'age' at 8
# delattr(emp1, 'age')  # Delete attribute 'age'
#
#
# if hasattr(emp1, 'age'):
#     print(getattr(emp1, 'age'))
# else:
#     print('no age attr')
# del emp1
# NameError: name 'emp1' is not defined
# if emp1:
#     print('emp1 is not null id is :%d  ' % id(emp1))
# else:
#     print('eml1 is null')

#
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# # Vector (7, 8)
# print(v1 + v2)

#
# class JustCounter:
#
#     # ADD TOW _  THAT __ IS MEANS PRIVATE
#     __secretCount = 0
#     secretCountB = 1
#
#     def count(self):
#         self.__secretCount += 1
#         print(self.__secretCount)
#         print(self.secretCountB)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# # print(counter.__secretCount)
# print(counter.secretCountB)
'''Python protects those members by internally changing the name to include the class name.
You can access such attributes as object._className__attrName. '''
# print(counter._JustCounter__secretCount)

import re

# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
#
# if searchObj:
#     print("searchObj.group() : ", searchObj.group())
#     print("searchObj.group(1) : ", searchObj.group(1))
#     print("searchObj.group(2) : ", searchObj.group(2))
# else:
#     print("Nothing found!!")

# phone = "2004-959-559 # This is Phone Number"
'''
Phone Num :  2004-959-559
Phone Num :  2004959559
'''
# Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print("Phone Num : ", num)

# Remove anything other than digits
# num = re.sub(r'\D', "", phone)
# print("Phone Num : ", num)
#
# import smtplib
#
# sender = '2627519719@qq.com'
# receivers = ['johnsonyanggao@gmail.com']
#
# message = """From: From Person <2627519719@qq.com>
# To: To Person <johnsonyanggao@gmail.com>
# Subject: SMTP e-mail test
#
# hello MR.Gao!
# This is a test e-mail message.
# """
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message)
#     print("Successfully sent email")
# except smtplib.SMTPException as e:
#     print("Error: unable to send email")

#
# import smtplib
# import base64
#
# filename = "/tmp/test.txt"
#
# # Read a file and encode it into base64 format
# fo = open(filename, "rb")
# filecontent = fo.read()
# encodedcontent = base64.b64encode(filecontent)  # base64
#
# sender = 'webmaster@tutorialpoint.com'
# reciever = 'amrood.admin@gmail.com'
#
# marker = "AUNIQUEMARKER"
#
# body = """
# This is a test email to send an attachement.
# """
# # Define the main headers.
# part1 = """From: From Person <me@fromdomain.net>
# To: To Person <amrood.admin@gmail.com>
# Subject: Sending Attachement
# MIME-Version: 1.0
# Content-Type: multipart/mixed; boundary=%s
# --%s
# """ % (marker, marker)
#
# # Define the message action
# part2 = """Content-Type: text/plain
# Content-Transfer-Encoding:8bit
#
# %s
# --%s
# """ % (body, marker)
#
# # Define the attachment section
# part3 = """Content-Type: multipart/mixed; name=\"%s\"
# Content-Transfer-Encoding:base64
# Content-Disposition: attachment; filename=%s
#
# %s
# --%s--
# """ % (filename, filename, encodedcontent, marker)
# message = part1 + part2 + part3
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, reciever, message)
#     print("Successfully sent email")
# except Exception:
#     print("Error: unable to send email")


# Regular Expressions

'''
\d any number
\D anything but a number
\s space
\b the whitespace around words
\. a period
\w any character

{1,3} we're expecting 1-3 #期待 数字位数最小为1位，最大为3位
+ Match one or more
? Match 0 or 1
* Match 0 or more
$ Match the end of a string
^ Matching the beginning of a string
| either or \d{1-3} | w{5-6}
[] range or 'variance' [A-Za-z]
{x} expecting 'x' amount


\n new line
\s space
\t tab
\e escape
\f form feed
\r return

'''
# import re
#
# expression = '''Jessica is 15 years old ,
# and Daniel is 28 years old ,Edward is 97 ,
# and his grandfather , Oscar ,is 120'''
#
# ages = re.findall(r'\d{1,3}', expression)
# names = re.findall(r'[A-Z][a-z]*', expression)
#
# print(ages)
# print(names)
#
# arg_data = {}
# x = 0
# for each_age in ages:
#     arg_data[each_age] = names[x]
#     x += 1
# # 特注:打印json并不是按顺序，而是随机 打印 key_value 对
# print(arg_data)




