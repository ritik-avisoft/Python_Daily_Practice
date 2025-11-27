from user_data_processor import *
proceed='y'
while proceed=='y':

    print(f'''
        Welcome to User Data Processor!
        {'--'*20} 
        Please provide the following details:
        1) To check user Data input and validation
        2) To perform safe division with favorite number 
        3) To read a file  
    ''')
    action=int(input("Enter the action number (1/2/3):- "))
    if action==1:
        user_data=get_user_details()
        if user_data:
            name, age, favorite_number = user_data
            print(f"User Details - Name: {name}, Age: {age}, Favorite Number: {favorite_number}")
    elif action==2:
        try:
            safe_division(user_data[2])
            # if user_data:
            #     name, age, favorite_number = user_data
            #     safe_division(favorite_number)
        except:
            print("Please get user details first by selecting action 1.")
    elif action==3:
        read_file()

    proceed=input("Do you want to continue? (y/n):- ").lower()
    if proceed == 'n':
        print("Thank you for using User Data Processor. Goodbye!")
        break
    elif proceed != 'y':
        print("Invalid input! Exiting the program.")
        break
