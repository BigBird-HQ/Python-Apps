list_of_contact = []
count = 0


def collect_user_details() -> dict:
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    phone_book = {
        "name": name,
        "phone_number": phone
    }

    list_of_contact.append(phone_book)

    return phone_book


if __name__ == '__main__':
    for contact in range(3):
        collect_user_details()

    print(list_of_contact)

    for index, eachContact in enumerate(list_of_contact):
        name = list_of_contact[index].get("name")
        phone = list_of_contact[index].get('phone_number')

        print(name + ": " + phone)