import admin_functions as admin
import student_functions as student
import teacher_functions as teacher

# from admin_functions import *
# from student_functions import *
# from teacher_functions import *


def main():
    while True:
        print("\n===== Student Resource Portal =====")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Teacher Login")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            admin.admin_menu()
        elif choice == '2':
            student.student_menu()
        elif choice == '3':
            teacher.teacher_menu()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
