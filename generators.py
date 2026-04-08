# generator 
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

for value in gen:
    print("Generated:", value)



# Using yield keyword
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print("Count:", num)



# List vs Generator
numbers_list = [i*i for i in range(5)]
print("List:", numbers_list)

numbers_gen = (i*i for i in range(5))
print("Generator:", numbers_gen)

for n in numbers_gen:
    print("Generated square:", n)



# Memory efficiency idea

def big_numbers():
    for i in range(1000000):
        yield i

# Only generates when needed
gen = big_numbers()
print("First value:", next(gen))
print("Second value:", next(gen))



# Generate numbers
def generate_numbers(n):
    for i in range(1, n+1):
        yield i

for num in generate_numbers(5):
    print("Number:", num)



# Fibonacci Generator

def fibonacci(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for f in fibonacci(7):
    print("Fibonacci:", f)