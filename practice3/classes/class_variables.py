#Properties are variables that belong to a class
#they store data for each object created from the class

#1
class Dog:
    species = "Canis familiaris"  #class variable(property)

    def __init__(self, name):
        self.name = name  #instance variable(property)

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.name)      # Buddy - instance variable
print(dog2.name)      # Charlie - instance variable
print(dog1.species)   # Canis familiaris - class variable
print(dog2.species)   # Canis familiaris - class variable

#2
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes" #change class property

print(p1.lastname) #Refsnes
print(p2.lastname) #Refsnes

#3
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25 #adding new property
p1.city = "Oslo" #adding new property

print(p1.name) #tobias
print(p1.age) #25
print(p1.city) #oslo

#4
class Dog:
    def __init__(self, name):
        self.name = name  #instance property

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

dog1.name = "Max"  #change instance variable only for dog1

print(dog1.name)  # Max
print(dog2.name)  # Charlie

#class variable is shared by all instances of a class
#while instance variable is unique to each object