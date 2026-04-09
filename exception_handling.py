# Basic try-except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("Invalid input")


# Handling specific exceptions
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


# Using else
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid number:", num)


# Using finally
try:
    print("Trying something...")
    x = 10 / 2
except:
    print("Error occurred")
finally:
    print("This always executes")



# Multiple exceptions together
try:
    num = int(input("Enter number: "))
    result = 100 / num
    print("Result:", result)
except (ValueError, ZeroDivisionError):
    print("Error: Invalid input or division by zero")


# Mini Project Calculator
def safe_calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            print("Result:", a / b)
        else:
            print("Invalid operation")

    except ValueError:
        print("Please enter valid numbers")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Calculation done")

safe_calculator()