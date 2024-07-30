# admin.py
import getpass
from quiz import Quiz

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        entered_username = input("Enter admin username: ")
        entered_password = getpass.getpass("Enter admin password: ")
        return entered_username == self.username and entered_password == self.password

    def add_questions(self, quiz):
        if self.authenticate():
            print("Authentication successful!")
            print("You can now add questions to the quiz.")
            while True:
                quiz.append_question()
                more_questions = input("Do you want to add another question? (yes/no): ").strip().lower()
                if more_questions != 'yes':
                    break
        else:
            print("Authentication failed. Access denied.")
