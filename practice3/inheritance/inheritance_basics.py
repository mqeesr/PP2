#Child class is the class that inherits from another class, also called derived class
#Any class can be a parent class, so the syntax is the same as creating any other class

#1
#class named Person, fname and lname properties, a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() #John Doe

#2
#Create a class named Student which will inherit 
#the properties and methods from the Person class
class Student(Person):
  pass 

#3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname() #Mike Olsen

#4
#class Student(Person):
  #def __init__(self, fname, lname):
    #add properties etc.

#When you add the __init__() function, the child class will
#no longer inherit the parent's __init__() function

#The childs __init__() function overrides the inheritance of the parents __init__() function

#5
#keep the inheritance of the parent's __init__() function
#and add a call to the parent's __init__() function
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 