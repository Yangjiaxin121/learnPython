#!/usr/bin/env/python3
# -*- coding:utf-8 -*-


class Student(object):

    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            return ValueError('bad score')

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 99, '男')
lisa = Student('Lisa Simpson', 87, '女')
bart.print_score()
lisa.print_score()
print(lisa.get_grade(),lisa.get_gender())
print(bart.get_grade(),bart.get_gender())

bart1 = Student('Bart',90, 'male')
if bart1.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')