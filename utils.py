def is_even(n):
    return n % 2 == 0

def find_max(a, b):
    return a if a > b else b

def square(n):
    return n * n

import utils

print(utils.is_even(4))
print(utils.find_max(10, 20))
print(utils.square(5))