Student_record_List = []
Student_info = {}
Scores = {}
Student_info = {}
Scores = {}
choice = True
loop = True

while loop:
    Operation = input("Enter the operation you want to perform (Fetch/Add): ")

    if Operation == "Add":
        while choice == True:
            Student_info["StudentName"] = input("Enter the Student full Name: ")
            Scores["Math"] = int(input("Enter the marks scored in math: "))
            Scores["Science"] = int(input("Enter the marks scored in science: "))
            Scores["English"] = int(input("Enter the marks scored in english: "))
            Student_info["Scores"] = Scores
            Student_record_List.append(Student_info)
            Student_info = {}
            Scores = {}
            answer = input("Do you want add one more student record? (Yes/No): ")
            if answer == "No":
                choice = False
                display = input("Do you want to display all student records? (Yes/No): ")
                if display == "Yes":
                    print(Student_record_List)

    elif Operation == "Fetch":
        Name = input("Enter the full name of the Student: ")
        for item in Student_record_List:
            if item["StudentName"] == Name:
                Subject = input("Enter the subject whose mark you want to fetch: ")
                scores = item["Scores"]
                print(f" The marks scored by {Name} in {Subject} is {scores[Subject]}")
            else:
                print("Entered student name is not available in the records")

    else:
        print("Entered Operation is incorrect. Please note that operation is case sensitive.")

    Breakpoint = input("Hit Enter to continue or Type Exit to close application: ")
    if Breakpoint == 'Exit':
        loop = False
