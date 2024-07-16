import student
import course

def main():
    while True:
        print("\nWelcome to Student Resource Portal")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Find Student")
        print("4. Display Courses")
        print("5. Add Course")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            grade = input("Enter student's grade: ")
            student.add_student(name, grade)
        
        elif choice == '2':
            student.display_students()
        
        elif choice == '3':
            name = input("Enter student's name to find: ")
            found_student = student.find_student(name)
            if found_student:
                print(f"Student found - Name: {found_student['name']}, Grade: {found_student['grade']}")
            else:
                print(f"Student '{name}' not found.")
        
        elif choice == '4':
            course.display_courses()
        
        elif choice == '5':
            new_course = input("Enter new course name to add: ")
            course.add_course(new_course)
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
