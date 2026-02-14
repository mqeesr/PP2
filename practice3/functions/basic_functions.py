#1
def my_function(): #def keyword used to define function
  print("Hello from a function") 

my_function() #calls a function

#2
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9 #functions can send data back to the code that called them using return statement

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50)) 

#3
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#4
def my_function():
  pass #pass allows you to define the structure first and implement details later(you cannot left func empty)