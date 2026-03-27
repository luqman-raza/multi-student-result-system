student = int(input("Enter number of students?"))
total_marks = 0
valid_students = 0

for i in range(student):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    if marks > 100 or marks < 0:
        print("You gave out-of-range marks. Please enter 0-100.")
    else:
        if marks >= 90:
            print(name, "- Grade A")
        elif 75 <= marks <= 89:
            print(name, "- Grade B")
        elif 50 <= marks <= 74:
            print(name, "- Grade C")
        else:
            print(name, "- Fail")

        total_marks += marks
        valid_students += 1


if valid_students > 0:
    average = total_marks / valid_students
    print("Average Marks:", average)
else:
    print("No valid student marks to calculate average.")