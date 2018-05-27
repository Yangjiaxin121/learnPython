

class Student(object):
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()
print(callable(Student('a')))