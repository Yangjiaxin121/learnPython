
class RunnableMaxIn(object):
    def run(self):
        print('Running....')

class FlyableMaxIn(object):
    def fly(self):
        print("Flying....")

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal,RunnableMaxIn):
    pass

class Bat(Mammal,FlyableMaxIn):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass




