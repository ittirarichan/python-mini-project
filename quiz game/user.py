class User:
    users = {}  

    @classmethod
    def register(cls):
        while True:
            username = input("Enter a username to register: ")
            if username in cls.users:
                print("Username already exists. Please try a different username.")
            else:
                break

        password = input("Enter a password: ")
        cls.users[username] = password
        print("Registration successful!\n")

    def _init_(self, username):
        self.username = username
        self.password = None

    def login(self):
        if self.username in User.users:
            self.password = input("Enter password: ")
            if User.users[self.username] == self.password:
                print("Login successful!\n")
                return True
            else:
                print("Incorrect password. Login failed.\n")
                return False
        else:
            print("Username not found. Please register first.\n")
            return False

    def take_quiz(self, quiz):
        if self.login():
            print(f"{self.username} is starting the quiz...\n")
            while not quiz.is_quiz_over():
                quiz.ask_question()
            print(f"Quiz over! {self.username}'s score: {quiz.get_score()}/{len(quiz.questions)}")
        else:
            print("Access denied. Unable to take the quiz.")