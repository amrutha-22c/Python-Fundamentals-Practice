# Raising exceptions
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    else:
        print("Access granted")

try:
    check_age(16)
except ValueError as e:
    print("Error:", e)



# Custom exception
class InvalidAmountError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InvalidAmountError("Insufficient balance")
    else:
        print("Withdraw successful")

try:
    withdraw(1000, 1500)
except InvalidAmountError as e:
    print("Custom Error:", e)


# Real scenario handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print("Division:", divide(10, 0))


# File Parser
def file_parser(filename):
    try:
        file = open(filename, "r")
        data = file.read()
        print("File Content:\n", data)
        file.close()

    except FileNotFoundError:
        print("Error: File not found")

    except Exception as e:
        print("Some error occurred:", e)

    finally:
        print("File operation completed")

file_parser("sample.txt")