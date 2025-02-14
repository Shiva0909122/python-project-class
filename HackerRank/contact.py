def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact {name} added successfully!\n")

def search_contact(contacts):
    name = input("Enter Name to Search: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}\n")
    else:
        print("Contact not found!\n")

def display_contacts(contacts):
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
        print()
    else:
        print("No contacts available!\n")

def main():
    contacts = {}
    while True:
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            display_contacts(contacts)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
