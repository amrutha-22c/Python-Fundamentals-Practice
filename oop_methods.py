# 1. Basic instance method
class Student1:
    def display(self):
        print("This is a student")

s1 = Student1()
s1.display()



# Accessing data using self
class Student2:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

s2 = Student2("Amrutha")
s2.show()



# Method with multiple data
class Student3:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, "scored", self.marks)

s3 = Student3("Ram", 90)
s3.display()



# Calling methods using objects
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

calc = Calculator()
print("Addition:", calc.add(5, 3))
print("Subtraction:", calc.sub(5, 3))



# Updating data using method
class Person:
    def __init__(self, name):
        self.name = name

    def update_name(self, new_name):
        self.name = new_name

    def display(self):
        print("Name:", self.name)

p = Person("Amrutha")
p.display()

p.update_name("Ammu")
p.display()



# example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()