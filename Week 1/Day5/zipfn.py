list1=["india","USA","Australia","hello"]
list2=["Delhi","New York","Sydne"]

s= zip(list1,list2)
s_dir=dict(s)
# print(s_dir)
for key,val in s_dir.items():
    print(key, ":", val)

