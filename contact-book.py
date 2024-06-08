# Task 5: Contact Book
contacts = {}


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added!")


def view_contacts():
    if not contacts:
        print("No contacts yet!")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {
                  details['email']}, Address: {details['address']}")


def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact updated!")
    else:
        print("Contact not found!")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found!")


def main():
    while True:
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
