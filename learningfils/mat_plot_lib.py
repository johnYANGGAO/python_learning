#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/10/16 3:43 PM
# @Author  : YangGao
# @File    : mat_plot_lib.py
import matplotlib.pyplot as plt
import numpy as np

'''1'''
'''ro->round'''
'''g->green'''

# # plt.plot([1, 2, 3, 4])
# # plt.ylabel('some numbers')
# plt.plot([1, 2, 3, 3.98], [1, 4, 9, 15.96], 'ro')
# # plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# # plt.axis([0, 6, 0, 20])
# plt.show()

'''2'''

#
# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
# plt.show()

# '''3'''
# plt.figure(1)  # the first figure
# plt.subplot(211)  # the first subplot in the first figure
# plt.plot([1, 2, 3])
# plt.subplot(212)  # the second subplot in the first figure
# plt.plot([4, 5, 6])
#
# plt.figure(2)  # a second figure
# plt.plot([4, 5, 6])  # creates a subplot(111) by default
#
# plt.figure(1)  # figure 1 current; subplot(212) still current
# plt.subplot(211)  # make subplot(211) in figure1 current
# plt.title('Easy as 1, 2, 3')  # subplot 211 title
# plt.show()

'''4'''
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
#
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
#
#
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

'''5'''
# ax = plt.subplot(111)
#
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# line, = plt.plot(t, s, lw=2)
#
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#              arrowprops=dict(facecolor='red', shrink=0.05),
#              )
#
# plt.ylim(-2, 2)
# plt.show()


'''6'''

# # make up some data in the interval ]0, 1[
# y = np.random.normal(loc=0.5, scale=0.4, size=1000)
# y = y[(y > 0) & (y < 1)]
# y.sort()
# x = np.arange(len(y))
#
# # plot with various axes scales
# plt.figure(1)
#
# # linear
# plt.subplot(221)
# plt.plot(x, y)
# plt.yscale('linear')
# plt.title('linear')
# plt.grid(True)
#
# # log
# plt.subplot(222)
# plt.plot(x, y)
# plt.yscale('log')
# plt.title('log')
# plt.grid(True)
#
# # symmetric log
# plt.subplot(223)
# plt.plot(x, y - y.mean())
# plt.yscale('symlog', linthreshy=0.05)
# plt.title('symlog')
# plt.grid(True)
#
# # logit
# plt.subplot(224)
# plt.plot(x, y)
# plt.yscale('logit')
# plt.title('logit')
# plt.grid(True)
#
# plt.show()
