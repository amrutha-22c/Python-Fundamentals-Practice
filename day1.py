# Program 1: Addition of two numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Sum:", a + b)


# Program 2: Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Program 3: Factorial
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

# 4: swap two numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)