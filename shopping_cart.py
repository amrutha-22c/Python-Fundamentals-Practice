# Shopping Cart System

cart = []

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        cart.append(item)
        print(item, "added to cart")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart")
        else:
            print("Item not found")

    elif choice == "3":
        print("Your Cart:")
        for i in cart:
            print("-", i)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")