'''Create a class called Student
Your class must have:
Attributes (inside __init__):
name
age
grade
Methods:
display_info() → prints all student details
is_passed() → return "Pass" if grade ≥ 40 else "Fail"
Your Task:
Create two Student objects
Call both methods for each student
'''
class Student:
    def __init__(self, name, age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.grade)
    
    def is_passed(self):
        return "pass" if self.grade>40 else "fail"
    

student1=Student("ritik",23,98)
student2=Student("raj",22,39)


student1.display_info()
print(student1.is_passed())
print("-"*10)
student2.display_info()
print(student2.is_passed())