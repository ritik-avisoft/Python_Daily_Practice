class Num:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def __add__(self,other):
        total=self.mark+other.mark   
        print(total)

n1=Num("ritik",23)
n2=Num("raj",33)
n3=Num("rishu",59)


# print(n1.mark+n2.mark+n3.mark)
print(n1+n3)
