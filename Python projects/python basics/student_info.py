# Step 1: Get the number of students
Student_count = int(input("How many student details you want to enter?:"))

# Step 2: collect
student_list = []
for i in range(Student_count):
    print(f"Enter details for student {i+1}:")
    Id = int(input("Student ID: "))
    name = input("Student name: ")
    age = int(input("Age: "))
    Math = float(input("Math marks: "))
    English = float(input("English marks: "))
    social_studies = float(input("Social Studies marks: "))
    Science = float(input("Science marks: "))
    Total_marks = Math + English + social_studies + Science
    Percentage = (Total_marks / 400) * 100
    if Percentage >= 90:
        grade = 'A'
    elif Percentage >= 80:
        grade = 'B'
    elif Percentage >= 70:
        grade = 'C'
    elif Percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    # Create a dictionary for each student
    student_info = {
        "Student ID": Id,
        "Name": name,
        "Age": age,
        "Math": Math,
        "English": English, 
        "Social Studies": social_studies,
        "Science": Science,
        "Total Marks": Total_marks,
        "Percentage": Percentage,
        "Grade": grade
    }
    
    # Append the dictionary to the student list
    student_list.append(student_info)

# Step 3: Ask for a student id to display details
search_id = int(input("Enter the Student ID to display details: "))
found = False
for student in student_list:
    if student["Student ID"] == search_id:
        print("Student Details:")
        for key, value in student.items():
            print(f"{key}: {value}")
        found = True
        break
if not found:
    print("Student ID not found.")

