

class Student(object):
    def __init__(self,name):
        self.__name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.__name

    __repr__ = __str__

print(Student('M'))
s = Student('S')