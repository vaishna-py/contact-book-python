def add_contact(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")
    print("Contact saved successfully.")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
            else:
                print("\n--- Contact List ---")
                for contact in contacts:
                    name, phone = contact.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contacts found.")

def main():
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
