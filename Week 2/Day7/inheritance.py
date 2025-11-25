# # parent to child cls 
# class parent():
#     def intellect(self):
#         print("A great thinking ability")
    
# class child(parent):
#     def patient(self):
#         print("low patient level")


# c=child()
# c.intellect()
# c.patient()

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):          # overriding
        print("Dog barks")


d=Dog()
a=Animal()

d.sound()
a.sound()
