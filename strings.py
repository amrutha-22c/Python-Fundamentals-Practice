text = "Hello Python"

print(text)
print(len(text))   
print(text[0])     
print(text[-1])    

# string slicing 
text = "Hello Python"

print(text[0:5])   
print(text[6:])    
print(text[::-1])  


# string methods
text = "  hello world  "

print(text.strip())      
print(text.upper())      
print(text.lower())      
print(text.capitalize()) 


# split and join
text = "apple,banana,mango"

fruits = text.split(",")
print(fruits)

joined = "-".join(fruits)
print(joined)


name = "Amrutha"
age = 20

print("Name:", name, "Age:", age)
print(f"Name: {name}, Age: {age}")

