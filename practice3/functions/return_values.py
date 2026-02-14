#1
def my_function(x, y):
  return x + y

result = my_function(5, 3) #x = 5, y = 3
print(result) #result will be 8

#2
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2]) 
"""
apple
banana
cherry
"""

#3

def my_function(name, /): #"/" is a positional argument
  print("Hello", name)

my_function("Emil") #my_function(name="Emil") mistake
#hello emil

#4
def my_function(*, name):
    print("Hello", name)
my_function(name="Emil") #my_function("Emil") mistake

#5
def my_function(a, b, /, *, c, d): #a, b, / positional; c, d keyword
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) #50