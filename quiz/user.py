
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")
        return entered_username == self.username and entered_password == self.password

    def take_quiz(self, quiz):
        if self.authenticate():
            print(f"{self.username} is starting the quiz...\n")
            while not quiz.is_quiz_over():
                quiz.ask_question()
            print(f"Quiz over! {self.username}'s score: {quiz.get_score()}/{len(quiz.questions)}")
        else:
            print("Authentication failed. Access denied.")
