student = {
    "name": "Amrutha",
    "age": 20,
    "course": "Python"
}

print(student["name"])
print(student["age"])

student = {"name": "Amrutha", "age": 20}

# add new key
student["grade"] = "A"

# update value
student["age"] = 21

print(student)

student = {"name": "Amrutha", "age": 20, "grade": "A"}

# remove using pop
student.pop("age")

# remove last item
student.popitem()

print(student)


student = {"name": "Amrutha", "age": 20, "grade": "A"}

for key, value in student.items():
    print(key, ":", value)


student = {"name": "Amrutha", "age": 20}

if "name" in student:
    print("Name exists")
else:
    print("Not found")


# create dictionary of squares

numbers = [1, 2, 3, 4, 5]

squares = {n: n*n for n in numbers}

print(squares)


students = {
    "s1": {"name": "Ram", "age": 20},
    "s2": {"name": "Sita", "age": 21}
}

print(students["s1"]["name"])

text = "apple banana apple orange banana apple"

words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)


