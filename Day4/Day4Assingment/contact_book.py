'''Assignment: Contact Book Using Dictionaries
Tasks
1. Create a Contact Book with at least five contacts.
Each contact name should be a key, and the value should be a nested dictionary
containing phone, email, and city.
2. Display All Contacts using dictionary keys, values, and items.
3. Search Features
   o Search by contact name.
   o Search by city (list all contacts from that city).
   o Partial name search (case-insensitive).
4. Add a New Contact and prevent duplicates based on name.
5. Update an Existing Contact (phone, email, or city).
6. Delete a Contact and show a message if it doesn’t exist.
'''

contacts = {
    "ritik": {
        "phone_no": "+91 1234567891",
        "email": "ritikkumar@email.com",
        "city": "Patna"
    },
    "raj": {
        "phone_no": "+91 1234567892",
        "email": "rajkumar@email.com",
        "city": "Banglore"
    },
    "ashu": {
        "phone_no": "+91 1234567893",
        "email": "ashukumar@email.com",
        "city": "Patna"
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

# for the Hardcoded values, this will only print at the begining of Project.. 
print("All Record's availave.... ")
for details in contacts.items():
                print(details)

process = 'y'
while process.lower() == 'y':
    print('''List for Action
1. Search Contact Detail's
2. Add New Detail's
3. Update Detail's
4. Delete Contact
5. All Record's
6. Search By key,Value,Items
''')


    choice_of_action = int(input("Choose what action you want to perform... "))
    if choice_of_action not in range(1,6):
        print("Please Enter Right Choice of Action ")
        
    # Search Contact Detail's
    if choice_of_action == 1:       
        print('''List for Search
1. Search by Contact Name
2. Search by City
3. Search by Partial Name
''')

        choice_for_search = int(input("Enter Choice for Search... "))

        # Search by Contact Name
        if choice_for_search == 1:              
            # print("Available Names:- ",contacts.keys())
            print("Available Names...")
            for nm in contacts.keys():
                print("--> ", nm)
            name = input("Enter the Name to Search from the above menu... ")
            if name in contacts:
                print(f"Details of {name}:")
                for key, value in contacts[name].items():
                    print(f"->    {key} : {value}")
            else:
                print("Contact not found.")

        # Search by City
        elif choice_for_search == 2:           
            print(f"Cities in the contact book... " )
            for name,info in contacts.items():
                print("  -->  ",info["city"])

            found = False
            city=input("enter city to search... ")
            for name, info in contacts.items():
                if info['city'] == city:
                    print(name, "->", info)
                    found = True
            if not found:
                print("No contacts found for this city.")

        # Search by Partial name Values
        elif choice_for_search == 3:            
            flag=False
            partial = input("Enter partial name to search.... ")
            for name, info in contacts.items():
                if partial in name:
                    print(name, "->", info)
                    flag=True
                if flag==False:
                    print("Not Found Any Contact by this Partial name..")
                    break
        else:
            print("Invalid Search Option")

    #Add New Detail's
    elif choice_of_action == 2:               
        new_name = input("Enter new name to add details... ")

        if new_name in contacts.keys():
            print(f"Duplicate Entry Can't allowed {new_name} already exist in contact book")
        else:
            ph_no = input("Enter Contact Number... ")
            while len(ph_no)<10 or len(ph_no)>10:
                print("Enter 10 Digit Number...")
                ph_no = input("Enter Contact Number... ")

            mail = input("Enter Email... ")
            while "@" not in mail:
                print("Enter Valid Email")
                mail = input("Enter Email... ")
            town = input("Enter City... ")

            contacts[new_name] = {
                "phone_no": ph_no,
                "email": mail,
                "city": town
            }

            print("New Record Added Successfully !!! ")

    #Update Detail's
    elif choice_of_action == 3:              
        # print("Available Names:- ",contacts.keys())
        
        
        name = input("Enter contact name to update: ")

        if name in contacts:
            print("What do you want to update?? (phone_no/email/city)")
            field = input("Enter field:")

            if field in contacts[name]:
                new_value = input(f"Enter new {field}: ")
                contacts[name][field] = new_value
                print("Contact Updated Successfully.")
            else:
                print("Invalid field.")
        else:
            print("Contact not found.")

    #TO Delete Contact  
    elif choice_of_action==4:           
        print("Available Names:- ",contacts.keys())
        name=input("Enter contact name to delete... ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Succesfully Deleted !!!")
        else:
            print("Contact Not Found !!!")

    #TO print All Record's
    elif choice_of_action==5:              
        for name,info in contacts.items():
            print("Name",name)
            for key,value in info.items():
                print("     ",key,":",value)

    #Search By key,Value,Items  
    elif choice_of_action==6:              
        print('''List for Search by {Key, Value, Items }
1. Search by Key
2. Search by Value
3. Search by Items
''')
        choice=int(input("By Which factor you want to search..." ))
        #Search by Key
        if choice==1:       
            for details in contacts.keys():
                print("Search By Key -> ", details)
        #Search by Value
        elif choice==2:
            for details in contacts.values():
                print("Search By Value -> ", details)
        #Search by Items
        elif choice==3:
            for details in contacts.items():
                print("Search By Item -> ", details)
        else:
            print("Choose Valid Input {1, 2, 3}")

    else:
        print("Choose Valid Input {1, 2, 3, 4, 5}")


    process = input("Want to proceed (y/n): ")