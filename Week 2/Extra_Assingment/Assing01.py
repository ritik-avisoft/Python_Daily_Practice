#write a program to input st name marks of 3 subject. print name & precentage in output

name=input("enter your name:- ")
sub1=int(input(f"welcome {name} Enter your obtained marks of sub 1.... "))
sub2=int(input(f"Enter your obtained marks of sub 2.... "))
sub3=int(input(f"Enter your obtained marks of sub 3.... "))

print(f'''Hello {name}
this is your sub1 mark's:-{sub1}
this is your sub2 mark's:-{sub2}
this is your sub3 mark's:-{sub3}
''')
sum_of_all_sub=sub1+sub2+sub3
percentage =( sum_of_all_sub/300) *100

print(percentage)
         
