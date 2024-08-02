from quiz import Quiz
from admin import Admin
from user import User

def main():
    quiz = Quiz()
    while True:
        role_choice = input(
            "Do you want to register/login as (1) User or (2) Admin? Enter 1 or 2: "
        ).strip()

        if role_choice == "1":
            user_action = input(
                "Do you want to (1) Register or (2) Login as a User? Enter 1 or 2: "
            ).strip()

            if user_action == "1":
                User.register()
            elif user_action == "2":
                username = input("Enter your username: ")
                user = User(username)
                user.take_quiz(quiz)
                break  
            else:
                print("Invalid choice. Please enter 1 or 2.")

        elif role_choice == "2":
            admin_action = input(
                "Do you want to (1) Register or (2) Login as an Admin? Enter 1 or 2: "
            ).strip()

            if admin_action == "1":
                Admin.register()
            elif admin_action == "2":
                username = input("Enter admin username: ")
                admin = Admin(username)  
                admin.add_questions(quiz)
                break  
            else:
                print("Invalid choice. Please enter 1 or 2.")

        else:
            print("Invalid choice. Please enter 1 or 2.")
main()
