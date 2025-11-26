# Online Course System 
class Course:
    plateform = "AviSkill"  # Class variable Same for all courses
    def __init__(self, course_name, instructor, duration):
        self.course_name = course_name  # Instance variable
        self.instructor = instructor    
        self.duration = int(duration)  # in months

    def display_details(self):
        print(f"Course Name: {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print(f"Duration: for {self.duration} month's")
        print(f"Platform: {Course.plateform}")

    def update_duration(self, new_duration):
        self.duration = new_duration
        print("=="*40)
        print(f"\nDuration updated to {self.duration} months for {self.course_name}🥳🎊")
        print("=="*40)
    def all_courses_on_platform(self):
        print(f"🎉 The course '{self.course_name}' is available on the '{Course.plateform}' platform.")

class ProgrammingCourses(Course):
    def __init__(self, course_name, instructor, duration, programming_language, difficulty_level):
        super().__init__(course_name, instructor, duration)  
        self.programming_language = programming_language    
        self.difficulty_level = difficulty_level          

    def display_details(self):  # Overriding method
        super().display_details()  
        print(f"Programming Language: {self.programming_language}")
        print(f"Difficulty Level: {self.difficulty_level}")

class DesignCourses(Course):
    def __init__(self, course_name, instructor, duration, software_used, difficulty_level):
        super().__init__(course_name, instructor, duration)  
        self.software_used = software_used
        self.difficulty_level = difficulty_level           

    def display_details(self):  
        super().display_details()   
        print(f"Software Used: {self.software_used}")
        print(f"Difficulty Level: {self.difficulty_level}")

    
#Demonstration of the classes and methods
prog_course1 = ProgrammingCourses("Python Basics", "Ritik kr Ranjan", 3, "Python", "Beginner")
design_course1 = DesignCourses("Graphic Design", "Harshit", 4, "Adobe Photoshop", "Intermediate")
prog_course2 = ProgrammingCourses("Advanced Java", "Karunesh", 5, "Java", "Advanced")
design_course2 = DesignCourses("UI/UX Design", "Raj", 6, "Figma", "Advanced")

# print(prog_course1.course_name)
# prog_course1.display_details()

#managing the list of object to print all at a time
course_type_list=[prog_course1,design_course1,prog_course2,design_course2]
# for i in course_type_list:
#     name_of_course=i.course_name
#     print(name_of_course)
print("=="*40)
print("🥳🥳Welcome to Your  Course management Plateform :- ")
print("=="*40)
proceed='y'
while proceed=='y':
    print("What type of action you want to perform?")
    print("1. Add New Course")
    print("2. Update Existing Course Duration")
    print("3. Display Course Details")
    print("4. Check the shared class variable thorugh changing the plateform name")
    print(f"5. All the courses are on the {Course.plateform} platform:- ") 
    print("--"*40)
    action=int(input("\nEnter the action number (1/2/3/4/5):- "))
    # print("--"*40)
    if action>5 or action<1:
        print("Invalid Action Selected!!")
        continue
    if action==1:
        #Taking input for the object creation
        print("=="*40)
        course_type=int(input("Enter the type of course you want to add (1) programming (2) design:- "))
        print("=="*40)
        if (course_type ==1 or course_type==2):   # handled isDigit with the help of chatGPT
            course_name=input("Enter the course name:- ")
            while any(char.isdigit() for char in course_name):
                print("course name should not contain numbers.")
                course_name = input("Enter the course name name again:- ")
            instructor = input("Enter the instructor name:- ")
            while any(char.isdigit() for char in instructor):
                print("Instructor name should not contain numbers.")
                instructor = input("Enter the instructor name again:- ")
            while True:
                duration_input = input("Enter the duration in months:- ")
                if duration_input.isdigit():      
                    duration = int(duration_input)
                    break                         
                else:
                    print("❌❌Invalid input! Duration must be an integer. Try again.")
            if course_type==1:
                valid_prog_lang=['java','pyhton','c++','js','sql','go','php','r']
                programming_language=input("Enter the programming language(java/python/c++/js/sql/go/php/r)):-  ")
                while programming_language not in valid_prog_lang:
                    print("Please enter Valid Language Again (java/python/c++/js/sql/go/php/r)")
                    programming_language=input("Enter the programming language(java/python/c++/js/sql/go/php/r)):-  ")

                valid_levels = ["Beginner", "Intermediate", "Advanced"]
                difficulty_level = input("Enter the difficulty level (Beginner/Intermediate/Advanced):- ")
                while difficulty_level not in valid_levels:
                    print("Invalid input! Difficulty level must be Beginner / Intermediate / Advanced only.")
                    difficulty_level = input("Enter the difficulty level again:- ")
                new_course=ProgrammingCourses(course_name, instructor, duration, programming_language, difficulty_level) #Creating object
                course_type_list.append(new_course)
                # course_name_list.append(course_name)
                print("=="*40)
                print("\nNew Programming Course Added Successfully!🥳🎊")
                print("=="*40)
                new_course.display_details()
            elif course_type==2:
                software_used=input("Enter the software used:- ")
                while any(char.isdigit() for char in course_name):
                    print("Software name should not contain numbers.")
                    course_name = input("Enter the Software used name again:- ")

                valid_levels = ["Beginner", "Intermediate", "Advanced"]
                difficulty_level = input("Enter the difficulty level (Beginner/Intermediate/Advanced):- ")
                while difficulty_level not in valid_levels:
                    print("Invalid input! Difficulty level must be Beginner / Intermediate / Advanced only.")
                    difficulty_level = input("Enter the difficulty level again:- ")

                new_course=DesignCourses(course_name, instructor, duration, software_used, difficulty_level) #Creating object
                course_type_list.append(new_course)
                # course_name_list.append(course_name)
                print("=="*40)
                print("\nNew Designing Course Added Successfully!🥳🎊")
                print("=="*40)
                new_course.display_details()
            else:
                print("❌❌Invalid course type entered!")
        else:
            print("😬Only Valid Course Types Are allowed (1 / 2) !!")
    elif action==2:
        course_name=input("\nEnter the course name to update duration:- ")
        found =False
        for course in course_type_list:
            in_list=course.course_name
            if in_list==course_name:
                new_duration=input(f"Enter the new Duration for the course {course_name}:- ")
                course.update_duration(new_duration)
                found=True
                break
        if not found:
                print("Course not found")

    elif action==3:
        course_name=input("\nEnter the course name to display details:- ")
        flag = False
        for course in course_type_list:
            course
            in_list=course.course_name
            if in_list==course_name:
                print("\n")
                course.display_details()
                flag=True
                break
                #handle edge case
        if not flag:
                print("Invalid Course Name")
    elif action==4:
        new_plateform=input("\nEnter the new platform name to update for all courses:- ")
        Course.plateform=new_plateform
        print(f"\nPlatform name updated to {Course.plateform} for all courses.🎊🥳")
    elif action==5:
        print("All courses ")
        print("=="*8)
        for course in course_type_list:
            # print("\n")
            course.all_courses_on_platform()

    proceed=input("\nwant to proceed (y/n):- ")