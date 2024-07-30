# main.py
from quiz import Quiz
from admin import Admin
from user import User

def main():
    quiz = Quiz()

    # Create an Admin with username and password
    admin = Admin("admin", "adminpass")

    # Admin login and question addition
    print("Admin Login:")
    admin.add_questions(quiz)

    # Create a User with username and password
    user = User("user", "userpass")

    # User login and taking the quiz
    print("\nUser Login:")
    user.take_quiz(quiz)

if __name__ == "__main__":
    main()
