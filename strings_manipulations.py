# Reverse a string
text = "Python"

reversed_text = text[::-1]
print("Reversed:", reversed_text)

# count vowels and consonants
text = input("Enter text: ").lower()

vowels = "aeiou"
v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)


# count words
text = input("Enter sentence: ")

words = text.split()
print("Word count:", len(words))


# Convert string to list of words
text = "I love Python"

words = text.split()
print(words)


# Remove duplicate characters
text = "programming"

result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)

