# print numbers from 1 to 10

for i in range(1, 11):
    if i == 5:
        continue   # skips 5
    if i == 8:
        break      # stops loop at 8
    
    print(i)

# pass example
for i in range(3):
    pass  # does nothing

