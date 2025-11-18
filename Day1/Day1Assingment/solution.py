print("BASIC CALCULATOR")

first_num=int(input("enter your first number:- "))
second_num=int(input("enter your Second number:- "))

print('''
Choose operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square
''')
ope=(int(input("Which operation you want to perform :- ")))

if ope==1:
    print(first_num + second_num)
elif ope==2:
    print(first_num - second_num)
elif ope==3:
    print(first_num * second_num)
elif ope==4:
    print(first_num / second_num)
elif ope==5:
    print(first_num ** second_num)
else:
    print("INVALID INPUT")



