# ask for age and have voter id and the check if user is eligible to vote 

age=int(input("enter your age: "))


if age<18:
        print("not eligible")
else:
    print('''
Are you a voter holder
      1. if yes
      2. if no
''')
    voter=int(input("do you have voter id card:- "))
    if voter==1:
        print("you can vote")
    else:
        print("apply for voter id")