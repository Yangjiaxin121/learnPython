#!/usr/bin/env/python3
# -*- coding:utf-8 -*-

def trim(s):
    if s == '':
        s = ''
    elif s[0] == ' ':
        n = len(s)
        s = trim(s[1:])
    elif s[-1] == ' ':
        n = len(s)
        s = trim(s[:-1])
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')