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
