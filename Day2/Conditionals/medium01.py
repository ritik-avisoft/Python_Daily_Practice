#ask user for two number and print which one is larger or if they are equal

f_num=int(input("enter first number:- "))
s_num=int(input("enter second number:- "))

if f_num>s_num:
    print("first num is greater")
elif s_num>f_num:
    print("second num is greater")
else:
    print("both are equal")