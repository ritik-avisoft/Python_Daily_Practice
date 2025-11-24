# main Python file

# Normal import
import mymodule
print("using normal import:")
print("--" * 20)
mymodule.default_parameter()
print("--" * 20)

# Specific function import
# print("--" * 20)
from mymodule import return_Imp_msg
print("\nusing specific function import:")

print("--" * 20)
user_preference = input("Do you want to receive an important message?(yes/no): ")
return_Imp_msg(user_preference)

# Alias import
import mymodule as mm
print("--" * 20)
print("\nusing alias import:")
print("--" * 20)
radius_input = float(input("Enter radius to calculate area: "))
area = mm.calculate_area(radius_input)
print(f"The area of circle of radius {radius_input} is: {area}")

# Using lambda function
print("--" * 20)
print("\nusing lambda function:")
print("--" * 20)
x = int(input("Enter first number to add: "))
y = int(input("Enter second number to add: "))
sum_result = mm.lambda_example(x, y)
print(f"The sum of {x} and {y} is: {sum_result}")

# Global variable
global_counter = 0
def update_counter():
    global global_counter
    global_counter += 1
    print("Global counter updated to:", global_counter)

import math
import random
# Using math module
print("--" * 20)
print("\nUsing math module:")
print("--" * 20)
number = int(math.sqrt(16))
print(f"The square root of 16 is: {number}")

# Using random module
print("\nUGenerating 4 Digit otp:")
print("--" * 20)
random_number = random.randint(1000, 10000)
print(f"Your generated 4 digit OTP is: {random_number}")
print("--" * 20)