#1
class MyClass:
  x = 5
print(MyClass) #<class '__main__.MyClass'>
#class with property x

#2
class MyClass:
  x = 5
p1 = MyClass()

print(p1.x) #5
#create an object named p1 and print x

#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1 #delete p1

print(p1) #traceback because we deleted p1

#4
class Person:
  pass
"""
same as for functions
class definitions cannot be empty
put in the pass statement to avoid getting an error
"""