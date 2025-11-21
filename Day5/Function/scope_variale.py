# # locav and global variable

# #local
# global_name="raju"
# def greet(name="Guest"):
#     # name="ritik"        #local variable
#     print("hello",name)
# # input_name=input("Enter Name: ")
# greet(global_name)


count = 0

def increase():
    global count    # i want to modify the global variable not to create another local
    count += 1

increase()
print(count)   # 1
