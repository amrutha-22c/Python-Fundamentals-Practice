
text = input("Enter a sentence: ")

words = text.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

sorted_words = sorted(frequency.items())

print("\nSorted Word Frequency:")
for word, count in sorted_words:
    print(word, ":", count)