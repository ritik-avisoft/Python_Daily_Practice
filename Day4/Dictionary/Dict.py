# #Dictionary
# print("Dictionary.............")
my_dic={'name':"ritik",
        "age":23,
        "State":"Bihar"}

# # print(my_dic['age'])
# print(my_dic.keys())
# print(my_dic.values())

# print(my_dic.items())

#------------------------------------------


# get : if key is not there then no err will shown 

# print(my_dic.get("age"))
# print(my_dic["roll"])

# print(my_dic("roll"))

#update 
print(my_dic)
my_dic.update({"State":"Jammu"})
print(my_dic)

my_dic.update({"payment":"Cash"})

print(my_dic)

my_dic.pop("payment")
print(my_dic)