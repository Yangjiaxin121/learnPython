


class Student(object):


    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

#s = Student()
#s.set_score(60)
#print(s.get_score())
#s.set_score(9999)

s = Student()
s.score = 60
print(s.score)
s.score = 99
print(s.score)
s.birth = 20
print(s.birth)
print(s.age)

