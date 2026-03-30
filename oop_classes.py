# Class definition
class Car:
    def show(self):
        print("This is a car")

# Object creation
c1 = Car()
c1.show()


class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# objects
car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")

print(car1.name, car1.color)
print(car2.name, car2.color)


# multiple objects
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, "scored", self.marks)

s1 = Student("Ram", 90)
s2 = Student("Sita", 95)

s1.display()
s2.display()

#basic calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

calc = Calculator()

print(calc.add(5, 3))
print(calc.sub(5, 3))