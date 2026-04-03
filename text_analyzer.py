# Text Analyzer Tool

text = input("Enter text: ")

# basic analysis
char_count = len(text)
words = text.split()
word_count = len(words)

# vowel count
vowels = "aeiouAEIOU"
vowel_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1

# results
print("\n--- Text Analysis ---")
print("Total characters:", char_count)
print("Total words:", word_count)
print("Total vowels:", vowel_count)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Reversed:", text[::-1])