#login authentiction for predefined user name 

user_name="ritik123"
password="Ritik@123"

print("Welcome to Login Page")
entered_username=input("Enter you user name... ")
if entered_username==user_name:
    print("Great Correct Username")
    entered_pass=input("enter your password now... ")
    if entered_pass== password:
        print("Login Successfully !!✨😃👍")
    else:
        entered_pass=input("enter your password Again... ")

else:
    entered_username=input("Enter you user name Again... ")
