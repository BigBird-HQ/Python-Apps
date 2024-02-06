class PhoneBook:
    contacts = {}

    def save_contact(self, contact, name):
        contact_to_save = {
            "name": name,
            "contact": contact
        }
        self.contacts[name] = contact_to_save
        return 'Contact saved!'

    def retrieve_contact(self, name):
        return self.contacts[name]['contact']


name = input('Enter the name to save ')
contact = input('Enter the number ')

phone_book = PhoneBook()

print(phone_book.save_contact(contact, name))