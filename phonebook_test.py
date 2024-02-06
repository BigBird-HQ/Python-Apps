import unittest

from PhoneBook import PhoneBook


class MyTestCase(unittest.TestCase):

    phonebook = PhoneBook()

    def test_something(self):

        contact = '09066665565'
        message = self.phonebook.save_contact(contact, "")
        expected = 'Contact saved!'
        self.assertEqual(expected, message) # add assertion here

    def test_contact_can_be_found(self):

        contact = '09066665565'
        name = "mich"

        message = self.phonebook.save_contact(contact, name)

        expected = 'Contact saved!'
        self.assertEqual(expected, message)

        found_contact = self.phonebook.retrieve_contact(name)
        self.assertEqual(contact, found_contact)

    def test_more_number_saved(self):
        contact1 = '09066665565'
        name1 = "mich"
        contact2 = '07064365565'
        name2 = "john"

        self.phonebook.save_contact(contact1, name1)
        self.phonebook.save_contact(contact2, name2)

        found_contact = self.phonebook.retrieve_contact(name1)
        self.assertEqual(contact1, found_contact)

if __name__ == '__main__':
    unittest.main()
