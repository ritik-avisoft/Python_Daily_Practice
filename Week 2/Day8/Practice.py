# # Global variable

# class MyClass:
#     def print_global_list(self):
#         print("Accessing global_list inside a method:", global_list)

#     def add_to_global_list(self, item):
#         global_list.append(item)
#         print("global_list after modification:", global_list)

# # Create an instance of MyClass
# global_list = [10, 20, 30]
# obj = MyClass()

# # Call methods to access and modify the global list
# obj.print_global_list()
# obj.add_to_global_list(40)
# obj.print_global_list()



def is_not_integer_string_try_except(input_string):
    try:
        int(input_string)
        print("its a numeric value")  # It IS an integer string
    except ValueError:
        return True  # It is NOT an integer string

# Example usage:
# print(is_not_integer_string_try_except("123"))   # False
# print(is_not_integer_string_try_except("-45"))   # False
# print(is_not_integer_string_try_except("12.5"))  # True
# print(is_not_integer_string_try_except("abc"))   # True

name= input("enter you name")
print(is_not_integer_string_try_except(name))