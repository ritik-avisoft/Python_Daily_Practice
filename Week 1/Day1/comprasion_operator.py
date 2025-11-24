#ask for the age and prit if the user is minor adult or senior
print("Verify your age for this game...")
age=int(input("Enter your age  "))

if age <18:
    print("you are minor Now Come later")
elif 18<=age<=60:
    print("you an Adult, Welcome to the game...")
else:
    print("Ohh Sry!! Yor Are too Old to play This....")