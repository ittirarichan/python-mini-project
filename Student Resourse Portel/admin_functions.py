students = []
teachers = []

def admin_menu():
    while True:
        print("\n===== Admin Menu =====")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. View All Students")
        print("4. View All Teachers")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            add_teacher()
        elif choice == '3':
            view_students()
        elif choice == '4':
            view_teachers()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

def add_student():
    name = input("Enter student's name: ")
    students.append(name)
    print(f"Student '{name}' added successfully.")

def add_teacher():
    name = input("Enter teacher's name: ")
    teachers.append(name)
    print(f"Teacher '{name}' added successfully.")

def view_students():
    print("\n=== List of Students ===")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. {student}")

def view_teachers():
    print("\n=== List of Teachers ===")
    for idx, teacher in enumerate(teachers, start=1):
        print(f"{idx}. {teacher}")