#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h = 1.75
w = 80.5
x = w/(h*h)
if x < 18.5:
    print('过轻')
elif x > 18.5 and x < 25:
    print('正常')
elif x > 25 and x < 28:
    print('过重')
elif x >28 and x < 32:
    print('肥胖')
else:
    print('严重肥胖')