#write a py prog for FiveDivisonError exception

class FiveDivisionError(Exception):
    def __init__(self):
        print("Can't divisible by 5 ")
    pass

try:
    n1=int(input("enter your first no :- "))
    n2=int(input("enter your second no :- "))
    if n2==5:
        raise FiveDivisionError #("Can not Allowed division by 5 ")
    res=n1/n2
    print(res)
# except Exception as obj:
#     print(obj)
except (FiveDivisionError,ZeroDivisionError) as var:
    print(var)


