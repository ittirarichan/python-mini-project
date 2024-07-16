courses = ["Math", "Science", "History"]

def display_courses():
    print("Available Courses:")
    for index, course in enumerate(courses, start=1):
        print(f"{index}. {course}")

def add_course(course):
    courses.append(course)
    print(f"Course {course} added successfully.")
