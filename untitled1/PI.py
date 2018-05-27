# -*- coding: utf-8 -*-
import itertools


def pi(N):
    #' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1)
    #natuals_list = list(natuals)
    #filter(lambda x:x%2==1,natuals_list)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x <= N, natuals)
    l = list(ns)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    for i in range(len(l)):
        l[i] = 2 * l[i] - 1
        if (i % 2 == 1):
            l[i] = 0 - l[i]
        l[i] = 4 / l[i]
    # step 4: 求和:
    return sum(l)

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
