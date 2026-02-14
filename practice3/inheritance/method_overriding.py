#1
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):  #method overriding
        print("Bark")

dog = Dog()
dog.sound()  #Bark (method in child class "overrids" the same method from parent class)

#2
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Driving a car")

c = Car()
c.move()

#3
class Printer:
    def print_document(self):
        print("Printing document...")

class ColorPrinter(Printer):
    def print_document(self):
        print("Printing document in color")

p = ColorPrinter()
p.print_document()  #Printing document in color