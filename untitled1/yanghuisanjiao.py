#!/usr/bin/python3
# -*- coding:utf-8 -*-


def triangles(max):
    L = [1]
    n = 1
    while n <= max:
        yield L
        n = n + 1
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


triangles = triangles(10)
for m in triangles:
    print(m)
