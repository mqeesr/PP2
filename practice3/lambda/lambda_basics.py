#1
x = lambda a : a + 10 #add 10 to argument a and return result
print(x(5)) #15

#2
x = lambda a, b : a * b #lambda cant take any num of arguments
print(x(5, 6)) #30

#3
def myfunc(n):
  return lambda a : a * n #function  that takes one argument and that argument will be multiplied with an unknown number

#4
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3) # n = 3, a will be 11(потом)

print(mytripler(11)) #33

#5
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #n = 2
mytripler = myfunc(3)#n = 3

print(mydoubler(11)) #22
print(mytripler(11)) #33