# 1. Basics of Set
numbers = {1, 2, 3, 4, 4, 5}  
print("Set:", numbers)


# 2. Adding Elements

numbers.add(6)  
numbers.update([7, 8, 9])  
print("After adding:", numbers)


# 3. Removing Elements

numbers.remove(1)   
numbers.discard(10) 
removed_item = numbers.pop()  
print("Removed item:", removed_item)
print("After removal:", numbers)


# 4. Set Operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)
print("Symmetric Difference:", a ^ b)


# 5. Looping Through Set

print("Looping:")
for item in a:
    print(item)


# 6. Checking Conditions

if 2 in a:
    print("2 is present in set a")

print("Length of set a:", len(a))


# 7. Set Methods

copy_set = a.copy()
print("Copied set:", copy_set)

copy_set.clear()
print("After clear:", copy_set)


# 8. Remove Duplicates (Real Use)

list_nums = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(list_nums))
print("Unique list:", unique_list)


# 9. Frozen Set
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)