class Student:
    def __init__(self, name, roll_no, age, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course
        self.marks = marks

    # Function 1
    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)

    # Function 2
    def show_marks(self):   
        print("Marks:", self.marks)


# Creating objects
S1 = Student("Ali", 101, 20, "AI", 85)
S2 = Student("Sara", 102, 21, "Computer Science", 78)
S3 = Student("Ahmed", 103, 19, "Data Science", 92)

# Calling functions
print("Student 1")
S1.display_info()
S1.show_marks()

print("\nStudent 2")
S2.display_info()
S2.show_marks()

print("\nStudent 3")
S3.display_info()
S3.show_marks()