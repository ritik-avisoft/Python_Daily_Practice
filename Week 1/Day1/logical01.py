print("LET'S CREATE YOUR ACCOUT TO ENTER THIS GAME")

user_id=input("create an User id :- ")
password=input("create your unique for this id:- ")

print("ACCOUNT SUCCESFULLY CREATED ")
print("ENTER LOGIN CREDENTION TO VISIT:- ")
login_id=input("Enter you id:- ")
login_password=input("Enter you password:- ")

if user_id==login_id and password==login_password:
    print("Great!!  You are Looged In")
elif user_id!=login_id and password!=login_password:
    print("both User Id and Pass Icorrect")
elif user_id!=login_id or password==login_password:
    print("Wrong user_id Please try again")
elif user_id==login_id or password!=login_password:
    print("Wrong password Please try again")

