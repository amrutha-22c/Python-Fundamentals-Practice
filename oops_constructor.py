# 1. Constructor basic
class Student1:
    def __init__(self):
        print("Constructor called")

s = Student1()



# 2. Using self keyword
class Student2:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

s1 = Student2("Amrutha")
s1.display()



# 3. Instance variables
class Student3:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s2 = Student3("Ram", 90)
print(s2.name, s2.marks)



# 4. Multiple objects
class Student4:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s3 = Student4("Ram", 90)
s4 = Student4("Sita", 95)

print(s3.name, s3.marks)
print(s4.name, s4.marks)



# 5. Method using instance variables
class Student5:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, "scored", self.marks)

s5 = Student5("Ram", 90)
s5.display()



# 6. Update instance variable
class Student6:
    def __init__(self, name):
        self.name = name

s6 = Student6("Amrutha")
print("Before:", s6.name)

s6.name = "Ammu"
print("After:", s6.name)



# 7. Real-world example (Car)
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(self.brand, "car is", self.color)

c1 = Car("BMW", "Black")
c2 = Car("Audi", "White")

c1.show()
c2.show()
