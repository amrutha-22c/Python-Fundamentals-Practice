import time
# Decorator with arguments
def my_decorator(func):
    def wrapper(a, b):
        print("Before execution")
        func(a, b)
        print("After execution")
    return wrapper

@my_decorator
def add(a, b):
    print("Sum:", a + b)

add(5, 3)


# Returning values from decorator
def my_decorator(func):
    def wrapper(a, b):
        result = func(a, b)
        return result
    return wrapper

@my_decorator
def multiply(a, b):
    return a * b

print("Result:", multiply(4, 5))


# Multiple decorators
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()


# Timer Decorator 
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start)
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function completed")

slow_function()