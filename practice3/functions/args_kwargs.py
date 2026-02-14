#1
def my_function(*kids): #*args allows to accept any number of arguments
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 
#The youngest child is Linus 

#2
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus") 
"""
Type: <class 'tuple'>
First argument: Emil
Second argument: Tobias
All arguments: ('Emil', 'Tobias', 'Linus')
"""

#3
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus") 
"""
Hello Emil
Hello Tobias
Hello Linus 
"""
#4
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5)) 
"""
6
100
5 
"""

#5
def my_function(**kid): #**kwargs allows to accept any number of keyword arguments
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 
#His last name is Refsnes

#6
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding") 
"""
username: emil123
additional details: 
age: 25
city: oslo
hobby: coding
"""

#7/8 unpacking * **
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) #same as my_function(1, 2, 3)
print(result) 

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # same as my_function(fname="Emil", lname="Refsnes")