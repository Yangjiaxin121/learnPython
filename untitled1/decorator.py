#!/usr/bin/env/python3
# -*- coding:utf-8 -*-


import functools
from datetime1 import time


def log(func):
    @functools.wraps(func)
    def metric(*args,**kw):
            print('%s executed in %s ms' % (func.__name__, 10.24))
            return func(*args,**kw)
    return metric


@log
def now():
    print('2015-3-25')


#print(now()())




@log
def fast(x, y):
    #time.sleep(0.0012)
    return x + y;


@log
def slow(x, y, z):
    #time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
