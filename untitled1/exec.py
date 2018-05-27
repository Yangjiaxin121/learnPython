#!/usr/bin/env/python3
# -*- coding:utf-8 -*-

from command import MyObject

computer = MyObject()

def run(x):
    inp = input('method>')
    #判断是否有这个属性
    if hasattr(computer,inp):
        func = getattr(computer,inp)
        print(func())
    else:
        setattr(computer,inp,lamba )
