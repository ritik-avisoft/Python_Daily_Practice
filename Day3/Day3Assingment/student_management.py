
print("Welcome to Student Management System")
student_name=[]
student_grade=[]
proceed='y'
##2 and 3 pe edge cases handle karna hai if student list is invalid then before entring any choices it should show that there s no any student

while proceed=='y':
    print('''
    Student Management Choices
    1. Add new Student
    2. Edit existing Student details
    3. Remove a Student from list
    4. display the record of all student 
    ''')

    valid_grade=['A','B','C','D','E','F','a','b','c','d','e','f']
    choice=int(input("Enter Your Choice to manage Student:- "))
    # print("Student Name","   ","Student grade")
    
    if choice<1 or choice>4:
        print("Wrong Choice !!! ")
    else:
        if choice==4:   #To Display all the Existing Student's Data
            if not student_name:
                print("List is empty")
            else:
                for st_name1, st_grade1 in zip(student_name,student_grade):#zip-> Use to aggrigate the elements from multiple iterables(list,tupples...)
                    print(st_name1,st_grade1)
          

        if choice==1:   #To Add new Student Record
            st_name,st_grade=input("Enter Student Name and Grade Saperated by Comma :- ").split(',')
            if st_name in student_name:
                print("Multiple entry not allowed with same name...")
            else:
                
                if st_grade not in valid_grade:
                    print("Please Enter Valid Grade 'a-f'..... ")
                else:
                    student_name.append(st_name)
                    student_grade.append(st_grade)
                    print("Added Successfully...")
  

        if choice==2:   #To Edit Grade Of Existing Student
            print("Choose the Existing student to make changes... ")
            for st_name1, st_grade1 in zip(student_name,student_grade):
                    # print("Student Name","   ","Student grade")
                    print(st_name1,st_grade1)
            choice_to_edit=input("Enter the name of Student Whome grade you want to edit:- ")
            if choice_to_edit in student_name:
                index=student_name.index(choice_to_edit)
                print("Valid Grade's\nA\nB\nC\nD\nE\nF")
                valid_grade=['A','B','C','D','E','F','a','b','c','d','e','f']
                new_grade=input("Enter the new Grade... ")
                if new_grade =="":
                     print("Grade Can't be null... ")
                elif new_grade not in valid_grade:
                     print("Invalid Grade Entered... ")
                else:
                    student_grade[index]=new_grade
            else:
                print("Student Not Exist in the List... ")


        if choice ==3:  #To Delete Existing Student Record
            print("Choose the Existing student to Delete... ")
            for st_name1, st_grade1 in zip(student_name,student_grade):
                    # print("Student Name","   ","Student grade")
                    print(st_name1,st_grade1)
            choice_to_del=input("Enter the name of Student name to delete:- ")
            index=student_name.index(choice_to_del)
            del student_name[index]
            del student_grade[index]

    proceed=input("Want to Proceed Further(y/n) ")

print("Invalid Input! Please Restart... ")
        