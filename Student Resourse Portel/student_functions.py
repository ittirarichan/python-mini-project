def student_menu():
    while True:
        print("\n===== Student Menu =====")
        print("1. View Courses")
        print("2. Enroll in a Course")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_courses()
        elif choice == '2':
            enroll_course()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def view_courses():
    print("\n=== Available Courses ===")
    # Define your course list or dictionary here
    courses = {
        'Math': ['Algebra', 'Geometry', 'Calculus'],
        'Science': ['Biology', 'Chemistry', 'Physics'],
        'Programming': ['Python', 'Java', 'C++']
    }
    for category, courses_list in courses.items():
        print(f"{category}: {', '.join(courses_list)}")

def enroll_course():
    course = input("Enter the course you want to enroll in: ")
    print(f"Enrolled in '{course}' successfully.")