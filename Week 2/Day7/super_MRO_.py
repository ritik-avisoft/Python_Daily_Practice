class Base:
    def show(self):
        pass   # Stops the chain safely

class A(Base):
    def show(self):
        print("A show")
        super().show()

class B(Base):
    def show(self):
        print("B show")
        super().show()

class C(A, B):
    def show(self):
        print("C show")
        super().show()

class D(C):
    def show(self):
        print("D show")
        super().show()

obj = D()
obj.show()
