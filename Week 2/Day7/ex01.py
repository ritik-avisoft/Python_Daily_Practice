# class Counter:
#     default_step = 1   # class variable

#     def __init__(self, start=0):
#         self.value = start  # instance variable

#     def increment(self, step=None):
#         if step is None:
#             step = Counter.default_step
#         self.value += step
#         return self.value

# c=Counter()
# print(c.increment())

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Animal makes a sound"


# class Cat(Animal):
#     def speak(self):
#         parent_sound = super().speak()     # call parent method
#         return f"{parent_sound}, {self.name} says Meow"


# class Dog(Animal):
#     def speak(self):
#         parent_sound = super().speak()
#         return f"{parent_sound}, {self.name} says Woof"


# cat = Cat("Billa")
# print(cat.speak())

# dog = Dog("Sheru")
# print(dog.speak())


class Animal:
    def sound(self):
        return "Animal makes a sound"

class Dog(Animal):
    def sound(self):
        # return "Dog bark"
        return super().sound() + ", Dog barks"

dog = Dog()
print(dog.sound())