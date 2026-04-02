# Basic Inheritance
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def display(self):
        print("This is child class")

c = Child()
c.show()
c.display()



# Parent & Child with constructor

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def show(self):
        print("Name:", self.name)

s = Student("Amrutha")
s.show()


# Using super() function

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

    def display(self):
        print(self.name, "is a", self.breed)

d = Dog("Tommy", "Labrador")
d.display()



# Types of Inheritance 
# Single Inheritance
class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

obj = B()
obj.method_a()
obj.method_b()


# Multilevel Inheritance
class X:
    def method_x(self):
        print("Class X")

class Y(X):
    def method_y(self):
        print("Class Y")

class Z(Y):
    def method_z(self):
        print("Class Z")

obj2 = Z()
obj2.method_x()
obj2.method_y()
obj2.method_z()


# example
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def type(self):
        print("This is a Car")

class Bike(Vehicle):
    def type(self):
        print("This is a Bike")

c1 = Car("BMW")
b1 = Bike("Yamaha")

c1.show()
c1.type()

b1.show()
b1.type()