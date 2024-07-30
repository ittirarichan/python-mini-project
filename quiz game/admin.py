import getpass

class Admin:
    admins = {} 

    @classmethod
    def register(cls):
        while True:
            username = input("Enter a username to register as admin: ")
            if username in cls.admins:
                print("Admin username already exists. Please try a different username.")
            else:
                break

        password = input("Enter a password: ")
        cls.admins[username] = password
        print("Admin registration successful!\n")

    def __init__(self, username):
        self.username = username
        self.password = None

    def login(self):
        entered_username = input("Enter admin username: ")
        entered_password = getpass.getpass("Enter admin password: ")

        if entered_username in Admin.admins and Admin.admins[entered_username] == entered_password:
            print("Login successful!\n")
            return True
        else:
            print("Authentication failed. Access denied.")
            return False

    def add_questions(self, quiz):
        if self.login():
            print("Authentication successful!")
            print("You can now add questions to the quiz.")
            while True:
                quiz.append_question()
                more_questions = input("Do you want to add another question? (yes/no): ").strip().lower()
                if more_questions != "yes":
                    break
        else:
            print("Authentication failed. Access denied.")
