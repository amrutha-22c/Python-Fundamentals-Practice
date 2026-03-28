import re
# 1. Basic search

text1 = "My number is 9876543210"
match = re.search(r"\d+", text1)

if match:
    print("Found number:", match.group())



# 2. Find all numbers

text2 = "Prices: 100, 250, 300"
numbers = re.findall(r"\d+", text2)
print("All numbers:", numbers)


# 3. Email validation

email = "user@gmail.com"

if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
    print("Valid Email")
else:
    print("Invalid Email")


# 4. Phone number validation

phone = "9876543210"

if re.fullmatch(r"\d{10}", phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")


# 5. Replace digits with *

text3 = "My number is 9876543210"
masked = re.sub(r"\d", "*", text3)
print("Masked text:", masked)


# 6. Extract words

text4 = "Hello world 123 Python"
words = re.findall(r"[a-zA-Z]+", text4)
print("Words:", words)


# 7. Password validation

password = "Abc12345"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")


# 8. Split using regex
text5 = "apple, banana; mango orange"
split_words = re.split(r"[,\s;]+", text5)
print("Split words:", split_words)


# 9. Remove special characters
text6 = "Hello@# World!! 123"
clean_text = re.sub(r"[^a-zA-Z0-9 ]", "", text6)
print("Clean text:", clean_text)