class Phonebook:
    def _init_(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        """Add a new contact to the phonebook."""
        self.contacts[name] = phone_number
        print(f"Contact for {name} added successfully.")

    def view_contacts(self):
        """Display all contacts in the phonebook."""
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts in Phonebook:")
            for name, phone_number in self.contacts.items():
                print(f"{name}: {phone_number}")

    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"No contact found for {name}.")

def main():
    phonebook = Phonebook()
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            phonebook.add_contact(name, phone_number)
        elif choice == '2':
            phonebook.view_contacts()
        elif choice == '3':
            name = input("Enter the name to search for: ")
            phonebook.search_contact(name)
        elif choice == '4':
            print("Exiting phonebook...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "_main_":
    main()



