# Nested Dictionary means dict inside a dict

student_data={
    "student1":{
        "name":"ritik",
        "grade":'A'
    },
    "student2":{
        "name":"raj",
        "grade":'A'
    },
    "student3":{
        "name":"ashu",
        "grade":'A'
    }
}

print(student_data)
# print(student_data.get("student1"))
# print(student_data.get("student2"))
# print(student_data.get("student3"))


print(student_data["student1"]["grade"])
print(student_data["student2"]["name"])

# updating the grade of student3
print("updating data")
student_data["student3"]["grade"]="A++"
print(student_data)

#adding data

student_data["student1"]["employeed"]="Yes"
print(student_data)

student_data["student2"]["employeed"]="Yes"
print(student_data)

student_data["student3"]["employeed"]="Yes"
print(student_data)

print(student_data.get("student1"))
print(student_data.get("student2"))
print(student_data.get("student3"))

student_data["student3"].pop("employeed")
print(student_data.get("student3"))

 


for name, grade in student_data.items():
    print("St:", name)
    for key, value in grade.items():
        print(key, ":", value)




print("-----next------")
a, b, c = (1, 2, 3)
print(a, b, c)