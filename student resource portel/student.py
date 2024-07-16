students = []

def add_student(name, grade):
    students.append({"name": name, "grade": grade})
    print(f"Student {name} added successfully.")

def display_students():
    if not students:
        print("No students registered yet.")
    else:
        print("List of Students:")
        for index, student in enumerate(students, start=1):
            print(f"{index}. Name: {student['name']}, Grade: {student['grade']}")

def find_student(name):
    for student in students:
        if student["name"] == name:
            return student
    return None
