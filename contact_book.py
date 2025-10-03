class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print(f"Contact with name '{name}' already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def search_contact(self, search_term):
        found_contacts = {name: details for name, details in self.contacts.items() 
                          if search_term.lower() in name.lower() or search_term in details['phone']}
        if not found_contacts:
            print(f"No contacts found for search term '{search_term}'.")
        else:
            print("\nSearch Results:")
            for name, details in found_contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self, name):
        if name not in self.contacts:
            print(f"Contact with name '{name}' does not exist.")
        else:
            print(f"Updating contact '{name}'. Leave fields blank to keep current values.")
            phone = input("Enter new phone number: ").strip() or self.contacts[name]['phone']
            email = input("Enter new email: ").strip() or self.contacts[name]['email']
            address = input("Enter new address: ").strip() or self.contacts[name]['address']
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact '{name}' updated successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact with name '{name}' does not exist.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ").strip()
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ").strip()
            contact_book.update_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ").strip()
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
