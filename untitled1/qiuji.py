#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
from functools import reduce

list(map(lambda s:s[:1].upper()+s[1:].lower(),['adam','LISA','barT']))
reduce(lambda x,y:x*y,[3,5,7,9])