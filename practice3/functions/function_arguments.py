#1
def my_function(name): #"name" is a parameter
  print("Hello", name)

my_function("Emil") #"emil" is an argument 

#2
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function() #if the function is called without an argument it uses the default value
my_function("Linus")

#3
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy") 
#i have a dog, mmy dog's name is buddy

#4
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person) 
"""
Name: Emil
Age: 25 
"""