contacts = {}

print("Customer Detail Book")
while True:
    print("\n1. Add a Contact")
    print("2. Display Contacts")
    print("3. Update Contact")
    print("4. Remove a Contact")
    print("5. Search for a Contact")
    print("6. Exit\n")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        email = input("Enter Email id: ")
        place = input("Enter your place: ")
        contacts[name] = {'number': number, 'email': email, 'place': place}
        print("{} added to contacts.".format(name))
    
    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            print("{:<20} {:<15} {:<30} {:<20}".format("Name", "Number", "Email", "Place"))
            for name, info in contacts.items():
                print("{:<20} {:<15} {:<30} {:<20}".format(name, info['number'], info['email'], info['place']))
    
    elif choice == '3':
        name = input('Enter name to update: ')
        if name in contacts:
            number = input('Enter new number: ')
            email = input('Enter new email: ')
            place = input('Enter new place: ')
            contacts[name]['number'] = number
            contacts[name]['email'] = email
            contacts[name]['place'] = place
            print(f"Contact '{name}' updated successfully.")
        else:
            print('Contact not found.')
    
    elif choice == '4':
        name = input("Enter contact name to remove: ")
        if name in contacts:
            del contacts[name]
            print("{} removed from contacts.".format(name))
        else:
            print("{} not found in contacts.".format(name))
    
    elif choice == '5':
        name = input("Enter contact name to search: ")
        if name in contacts:
            print("Name: {}, Number: {}, Email: {}, Place: {}".format(name, contacts[name]['number'], contacts[name]['email'], contacts[name]['place']))
        else:
            print("{} not found in contacts.".format(name))
    
    elif choice == '6':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
