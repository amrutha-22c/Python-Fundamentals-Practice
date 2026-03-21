# function without parameters

def greet():
    print("Hello, welcome!")

greet()

def add(a, b):
    print("Sum:", a + b)

add(5, 3)

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Result:", result)

#modules
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

#use it in another file
import mymath

print(mymath.add(10, 5))
print(mymath.subtract(10, 5))