#!/usr/bin/env/python3
# -*- coding:utf-8 -*-


def find_min_and_max(L):

    if len(L) == 0:
        return None, None
    a = L[0]
    b = L[0]

    for x in L:
        if x < a:
            a = x
        if x > b:
            b = x
    return a, b


#L = [1, 3, 5, 4]
#print(find_min_and_max(L))


if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')