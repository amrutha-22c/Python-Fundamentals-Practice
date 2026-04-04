# Public vs Private Variables
class Person:
    def __init__(self, name, age):
        self.name = name       
        self.__age = age        

p = Person("Amrutha", 20)

print("Public:", p.name)




# Name Mangling
class Demo:
    def __init__(self):
        self.__value = 100

d = Demo()

print("Private using mangling:", d._Demo__value)



# Getter and Setter Methods
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid marks")

s = Student(90)

print("Marks:", s.get_marks())

s.set_marks(95)
print("Updated Marks:", s.get_marks())



# @property decorator
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Invalid salary")

e = Employee(50000)

print("Salary:", e.salary)

e.salary = 60000
print("Updated Salary:", e.salary)



# Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.get_balance())