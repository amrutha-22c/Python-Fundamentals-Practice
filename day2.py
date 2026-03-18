a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest is:", a)
elif b >= a and b >= c:
    print("Greatest is:", b)
else:
    print("Greatest is:", c)
    
 # celsius to fahrenheit
 celsius = float(input("Enter temperature in Celsius: "))
 fahrenheit = (celsius * 9/5) + 32
 print("Temperature in Fahrenheit:", fahrenheit)
 
 #simple Interest
 p = float(input("Enter principal amount: "))
 r = float(input("Enter rate of interest: "))
 t = float(input("Enter time in years: "))
    si = (p * r * t) / 100
    print("Simple Interest:", si)