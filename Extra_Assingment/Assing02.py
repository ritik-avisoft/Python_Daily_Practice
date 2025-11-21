#Write a python program that collect multiple types of data(e.g., name, age, height, and student status) from user input, store them in a dictionary, and print out the collected data.\

st_dict={}
name=input("enter your name... ")
age=int(input("enter your age... "))
height=float(input("enter your hright in cm (e.g., -> 180.00)... "))
status=input("enter your status... ")

st_dict["Name"]=name
st_dict["Age"]=age
st_dict["Height"]=height
st_dict["Status"]=status

# print(st_dict.items())
print("--" * 30)
print("     ","Your Complete detail's..")
print("--" * 30)
for key, Value in st_dict.items():
    print(f"    ",key,":",Value)
print("--" * 30)
print("     ","Thank You..")
print("--" * 30)