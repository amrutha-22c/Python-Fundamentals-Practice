# list operations

items = ["apple", "banana", "milk"]

# add item
items.append("bread")

# insert item
items.insert(1, "eggs")

# remove item
items.remove("banana")

print("Final list:", items)


# shopping cart total

prices = [100, 200, 50, 150]

total = 0

for price in prices:
    total += price

print("Total price:", total)

tweets = ["tweet1", "tweet2", "tweet3", "tweet4", "tweet5"]

# get first 3 tweets
print("Feed:", tweets[:3])

# square numbers

numbers = [1, 2, 3, 4, 5]

squares = [n*n for n in numbers]

print("Squares:", squares)

# tuple example

coordinates = (10, 20)

print("X:", coordinates[0])
print("Y:", coordinates[1])

point = (5, 7)

x, y = point

print("x =", x)
print("y =", y)

