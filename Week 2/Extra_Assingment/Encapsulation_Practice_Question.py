class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self._department=department
        self.__salary=salary
    def display_info(self):
        print(f"Your Name is '{self.name}' and you are in '{self._department}' department earning '{self.__salary}' monthly.")
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print(f"Salary updated to {self.__salary}")
        else:
            print("Invalid salary amount!")
    
e1=Employee('ritik','it',50000)
print("\n")
e1.display_info()
print("Accessing protected attribute:", e1._department)
# print(e1.__salary) # we can't have the direct access to the private attribute
print("Current Salary:", e1.get_salary())

e1.set_salary(60000)
e1.display_info()
