def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

import calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1.Add  2.Sub  3.Mul  4.Div")
choice = int(input("Choose: "))

if choice == 1:
    print(calculator.add(a, b))
elif choice == 2:
    print(calculator.sub(a, b))
elif choice == 3:
    print(calculator.mul(a, b))
elif choice == 4:
    print(calculator.div(a, b))
else:
    print("Invalid choice")