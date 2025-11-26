'''
## 🎯 **Assignment Goal**
Create a small Course Management System using **OOP concepts** like:
* Inheritance
* Method overriding
* `super()`
* Class variable vs instance variable
### 🔹 **Step 1: Make a Parent Class**
Create a class called **Course**.
This class should have:
* course_name  (instance variable)
* instructor   (instance variable)
* duration     (instance variable)
* platform = "SkillUp" (class variable — same for all courses)

Methods required:

* **display_details()** → show course information
* **update_duration(new_duration)** → change course duration

---

### 🔹 **Step 2: Make Child Classes**

Create **two classes that inherit from Course**, for example:

* ProgrammingCourse
* DesignCourse

These classes:

* Should have **extra attributes**, unique for the course type (example: programming language, software used, difficulty level, etc.)
* Must **override the display_details() method**
* Must use **super()** to reuse parent class code

---

### 🔹 **Step 3: Test the Program**

Do the following in your main code:

✔ Create **multiple objects** of both child classes
✔ Call methods from both **parent and child classes**
✔ Update some values (like duration) and print results again
✔ Show that **class variable (platform name)** is shared by all objects
  → Example: changing Course.platform affects all courses

---

## 💡 Final Output Expectations (in simple words)

Your output should clearly show:

| Concept            | Shown by                                       |
| ------------------ | ---------------------------------------------- |
| Inheritance        | child classes using parent properties          |
| Method overriding  | child modifies display_details()               |
| super()            | child calls parent method                      |
| Class variable     | platform same for all courses                  |
| Instance variables | name, instructor, duration stored individually |

'''

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
        print(f"Duration updated to {self.duration} hours for {self.course_name}")

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

# Displaying details
print("\nDisplaying the details for all courses:")
print("=="*22)
print("\nProgramming Course 1 Details:")
print("--"*15)
prog_course1.display_details()
print("\nDesigning Course 1 Details:")
print("--"*15)
design_course1.display_details()
print("\nProgramming Course 2 Details:")
print("--"*15)
prog_course2.display_details()
print("\nDesigning Course 2 Details:")
print("--"*15)
design_course2.display_details()
print("\n")

# Updating duration
print("\nUpdating Duration for courses...")
print("=="*15)
prog_course1.update_duration(11)
design_course1.update_duration(10)
print("--"*15)
print("After Updating Duration:")
print("--"*15)
prog_course1.display_details()
print("--"*15)
design_course1.display_details()

# Showing class variable is shared
print("=="*20)
Course.plateform = "R's Academy"


print("\nChanging platform name for all courses...")
print("\nAfter Changing Course 1 Platform Name:")
print("--"*15)
prog_course1.display_details()
print("\nAfter Changing Course 2 Platform Name:")
print("--"*15)
design_course1.display_details()
    
            