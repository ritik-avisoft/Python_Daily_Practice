# this is my module having four function

#Functions with Default parameter
def default_parameter(name="User"):
    print("Welcome", name)

# Function with input parameter and also retrunig a useful message
def return_Imp_msg(preferance):
    if preferance=="yes":
        print('''Keep exploring, keep asking questions, and keep building.
Every task you complete is a step toward real industry experience. Stay
curious and take your internship as an opportunity to grow.''')
    else:
        print("No important message for you")

# Function to calculate area of circle by taking radius as input
def calculate_area(radius):
    pi=3.14
    area=pi*radius*radius
    return area

# Lambda function example by taking two input.

def lambda_example(x, y):
    add = lambda a, b: a + b
    return add(x, y)