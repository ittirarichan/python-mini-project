def teacher_menu():
    while True:
        print("\n===== Teacher Menu =====")
        print("1. View Assigned Courses")
        print("2. Grade Student")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_assigned_courses()
        elif choice == '2':
            grade_student()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def view_assigned_courses():
    print("\n=== Assigned Courses ===")
    # Implement logic to fetch assigned courses for the teacher
    assigned_courses = ['Algebra', 'Biology']
    for course in assigned_courses:
        print(course)

def grade_student():
    student_name = input("Enter student's name to grade: ")
    grade = input("Enter grade for the student: ")
    print(f"Grade '{grade}' recorded for student '{student_name}'.")