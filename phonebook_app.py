# Phonebook Application

phonebook = {}

while True:
    print("\n--- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact added!")

    # View Contacts
    elif choice == "2":
        if not phonebook:
            print("Phonebook is empty")
        else:
            for name, number in phonebook.items():
                print(name, ":", number)

    # Search Contact
    elif choice == "3":
        name = input("Enter name to search: ")
        number = phonebook.get(name)
        if number:
            print("Number:", number)
        else:
            print("Contact not found")

    # Update Contact
    elif choice == "4":
        name = input("Enter name to update: ")
        if name in phonebook:
            new_number = input("Enter new number: ")
            phonebook[name] = new_number
            print("Contact updated")
        else:
            print("Contact not found")

    # Delete Contact
    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in phonebook:
            phonebook.pop(name)
            print("Contact deleted")
        else:
            print("Contact not found")

    # Exit
    elif choice == "6":
        print("Exiting Phonebook...")
        break

    else:
        print("Invalid choice")