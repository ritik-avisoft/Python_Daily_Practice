# list i a mutable type , in list we can store multi type data,

#syntax
number = [1,2,3,4,5]
alphabets=['a','b','c','d','e']
name=["ritik","karu","harshit"]

print("Append and Insert function............")
# we can add ele in list after creation using "Append and Insert function".

number.append(6)
print(number)

print("concatination............")
#we can merg or add two list using concatination
merged_list = number + alphabets
print(merged_list)

print("NEXT SOLUTION............")
#range function , if want to print all ele from an list 

for i in merged_list:
    print(i)
  

print("NEXT SOLUTION............")

#USE OF LENGTH FUNCTION 

print(len(merged_list))


print("NEXT SOLUTION............")
#removing element using POP and DEL
popped_ele=number.pop(-2)
print(popped_ele)
print("NEXT SOLUTION.....DEL.......")

del number[1]
print(number)                                                                                                                                                                                                                                                                                                       

print("NEXT SOLUTION......CLEAR......")
# Clear is use to delete all item from a list
name.clear()
print(name)


#adding two or more list using add and extend fn 

list1=[1,2,3,4,5]
list2=['a','b','c','d']

list3 = list1 + list2
print(list3)

list3.extend(list1)
print(list3)
list1.extend(list2)
print(list1)