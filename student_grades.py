student_grades = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student Grade")
    print("3. Print All Student Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        student_grades[name] = grade
        print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        if student_grades:
            print("\nStudent Grades:")
            for name, grade in student_grades.items():
                print(name, ":", grade)
        else:
            print("No student records available.")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")