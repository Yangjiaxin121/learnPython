#!/usr/bin/env/python3
# -*- coding:utf-8 -*-

L = [('Bob', 75),('Adam', 92),('Bart', 66),('Lisa', 88)]


def by_score(t):
    return t[-1]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_score,reverse=True)
L3 = sorted(L, key=by_name)
print(L2)
print(L3)