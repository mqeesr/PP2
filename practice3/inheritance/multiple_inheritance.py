#multiple inheritance is when class inherits свойства и
#методы сразу от нескольких родительских классов

#1
class Flyer:
    def fly(self):
        print("I can fly")

class Swimmer:
    def swim(self):
        print("I can swim")

class Duck(Flyer, Swimmer):  #multiple inheritance
    pass

d = Duck()
d.fly()#I can fly
d.swim()#I can swim

#2
class Phone:
    def call(self):
        print("Making a call")

class Camera:
    def take_photo(self):
        print("Taking a photo")

class SmartPhone(Phone, Camera):
    def info(self):
        print("I am a smartphone")
        self.call()
        self.take_photo()

s = SmartPhone()
s.info()
"""
I am a smartphone
Making a call
Taking a photo
"""

#3
class Walker:
    def walk(self):
        print("I can walk")

class Jumper:
    def jump(self):
        print("I can jump")

class Flyer:
    def fly(self):
        print("I can fly")

class SuperAnimal(Walker, Jumper, Flyer):
    def show_abilities(self):
        self.walk()
        self.jump()
        self.fly()
        print("I am super")

sa = SuperAnimal()
sa.show_abilities()

"""
I can walk
I can jump
I can fly
I am super
"""