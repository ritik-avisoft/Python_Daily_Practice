# defining fn 

def print_sum(m,n):
    print("Sum of m and n is :- ", m + n)

a,b=(input("enter two numbers saperatd by , ")).split(',')
a=int(a)
b=int(b)
print_sum(a,b)