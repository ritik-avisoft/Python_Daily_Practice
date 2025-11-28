#geting user details and handling exceptions by import from exception_handled.py
from exception_handled import InvalidAgeError, InvalidFavoriteNumberError, NameContainsNumberError
def get_user_details():
        while True:     # storage method , we need to store the right value.
            try:
                name = input("Enter your name: ")
                #name validation must not contains any number's its cant be Empty 
                if name.strip() == "":
                    raise NameContainsNumberError("Name cannot be empty.")
                if any(char.isdigit() for char in name):
                    raise NameContainsNumberError("Name should not contain numbers.")

                # Validate age
                age_input = input("Enter your age: ")
                if age_input.strip() == "":
                    raise InvalidAgeError("Age cannot be empty.")
                if not age_input.isdigit():
                    raise InvalidAgeError("Age must be a valid +ve integer.") #handled age shuld not be anything other than integer
                age = int(age_input)
                if age < 18 or age > 120:
                    raise InvalidAgeError("Age must be between 18 and 120.")
                

                #validate favorite number for 0 and -ve numbers and also cant be empty 
                favorite_number_input = input("Enter your favorite number: ")
                if favorite_number_input.strip() == "":
                    raise InvalidFavoriteNumberError("Favorite number cannot be empty.")
                if not favorite_number_input.isdigit():
                    raise InvalidFavoriteNumberError("Favorite number should not ba a String.")
                favorite_number = int(favorite_number_input)
                if favorite_number <= 0:
                    raise InvalidFavoriteNumberError(favorite_number, "Favorite number must be a positive integer greater than zero.")

                return name, age, favorite_number #returning the valid details 
            except (InvalidAgeError, InvalidFavoriteNumberError, NameContainsNumberError) as custom_err:
                print(f"Custom Error: {custom_err}")
                return get_user_details()  # Retry getting user details

# Safe division function
def safe_division(favorite_number):
    try:
        result = 100 / favorite_number
        print(f"100 divided by your favorite number {favorite_number} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Favorite number must be a number.")

# File handling function for already created files.
def read_file():
    file = input("Enter the filename to read: ")
    try:
        if file.lower().strip() == "secret1.txt":
            raise PermissionError("Access to this file is denied.")
        
        with open(file, 'r') as f:
            content = f.read()
            print("File Content:")
            print("--" * 20)
            print(content)
            print("--" * 20)
            
    except FileNotFoundError:
        print("Custom_Error: The file does not exist.")
    except PermissionError:
        print("Custom_Error: You do not have permission to read this file.")
    
    finally:
        print("File operation complete.")
        
