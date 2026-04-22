contacts = {}

def add_contact(name, phone):
    if not phone.isdigit():
        print("Phone number must contain only digits.")
        return
    if len(phone) != 10:
        print("Phone number must be exactly 10 digits.")
        return

    contacts[name] = phone
    print(f"Added {name}: {phone}")
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():1
            print(f"{name}: {phone}")

def main():
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()