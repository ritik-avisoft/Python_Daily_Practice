"""
Assignment: Contact Book Using Dictionaries
"""

contacts = {
    "ritik": {
        "phone_no": "+91 1234567891",
        "email": "ritikkumar@email.com",
        "city": "Patna"
    },
    "raj": {
        "phone_no": "+91 1234567892",
        "email": "rajkumar@email.com",
        "city": "Bangalore"
    },
    "ashu": {
        "phone_no": "+91 1234567893",
        "email": "ashukumar@email.com",
        "city": "Punjab"
    },
    "karu": {
        "phone_no": "+91 1234567894",
        "email": "karukumar@email.com",
        "city": "Jammu"
    },
    "harsh": {
        "phone_no": "+91 1234567895",
        "email": "harshkumar@email.com",
        "city": "Kashmir"
    }
}

process = 'y'

while process.lower() == 'y':
    print("""
List for Action
1. Search Contact Details
2. Add New Contact
3. Update Contact
4. Delete Contact
""")

    choice_of_action = int(input("Choose what action you want to perform: "))

    if choice_of_action == 1:
        print("""
List for Search
1. Search by Contact Name
2. Search by City
3. Search by Partial Name
""")

        choice_for_search = int(input("Enter Choice for Search: "))

        # Search by Name
        if choice_for_search == 1:
            # print("Available Contacts:", ', '.join(contacts.keys()))
            print("Available Contacts", contacts.keys())
            name = input("Enter the Name to Search: ").lower()

            if name in contacts:
                print(f"Details of {name}:")
                for key, value in contacts[name].items():
                    print(f"  {key} : {value}")
            else:
                print("Contact not found.")

        # Search by City
        elif choice_for_search == 2:
            city = input("Enter City to search: ").lower()
            found = False
            for name, info in contacts.items():
                if info['city'].lower() == city:
                    print(name, "->", info)
                    found = True
            if not found:
                print("No contacts found in this city.")

        # Search by Partial Name
        elif choice_for_search == 3:
            part = input("Enter partial name to search: ").lower()
            for name, info in contacts.items():
                if part in name.lower():
                    print(name, "->", info)
        else:
            print("Invalid Search Option")

    elif choice_of_action == 2:
        new_name = input("Enter new name to add: ").lower()

        if new_name in contacts:
            print(f"Duplicate Entry Not Allowed. {new_name} already exists.")
        else:
            ph_no = input("Enter Contact Number: ")
            mail = input("Enter Email: ")
            town = input("Enter City: ")

            contacts[new_name] = {
                "phone_no": ph_no,
                "email": mail,
                "city": town
            }
            print("New Record Added Successfully !!!")

    elif choice_of_action == 3:
        name = input("Enter contact name to update: ").lower()

        if name in contacts:
            print("What do you want to update? (phone/email/city)")
            field = input("Enter field: ").lower()

            if field in contacts[name]:
                new_value = input(f"Enter new {field}: ")
                contacts[name][field] = new_value
                print("Contact Updated Successfully.")
            else:
                print("Invalid field.")
        else:
            print("Contact not found.")

    # ================= DELETE =================
    elif choice_of_action == 4:
        name = input("Enter contact name to delete: ").lower()

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully.")
        else:
            print("Contact not found.")

    else:
        print("Choose Valid Input {1, 2, 3, 4}")

    process = input("Want to proceed (y/n)? : ")