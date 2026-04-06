# Function inside function
def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()



# Returning function
def outer_func():
    def inner_func():
        print("Hello from inner")
    return inner_func

f = outer_func()
f()



# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def say_hello():
    print("Hello!")

decorated = my_decorator(say_hello)
decorated()



# Using @ decorator syntax
def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@my_decorator
def greet():
    print("Welcome!")

greet()


# Decorator with arguments
def my_decorator(func):
    def wrapper(name):
        print("Before execution")
        func(name)
        print("After execution")
    return wrapper

@my_decorator
def greet_user(name):
    print("Hello", name)
greet_user("Amrutha")