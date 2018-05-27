#!/usr/bin/env/python3
# -*- coding:utf-8 -*-


class MyObject(object):
    def __init__(self):
        self.x = 9


    def add(self):
        return self.x + self.x

    
    def pow(self):
        return self.x*self.x


    def power(self):
        return self.x - self.x


    def div(self):
        return self.x/self.x
