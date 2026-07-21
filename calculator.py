# Simple Calculator and grading calculator
print ("Welcome to the Grading Calculator!")
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)