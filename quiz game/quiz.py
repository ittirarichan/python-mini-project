from question import Question

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def append_question(self):
        question_text = input("Enter the question: ")
        options = []
        for i in range(4):  # Assuming 4 options for simplicity
            option = input(f"Enter option {i + 1}: ")
            options.append(option)
        while True:
            try:
                correct_option_index = (
                    int(input("Enter the number of the correct option (1-4): ")) - 1
                )
                if correct_option_index < 0 or correct_option_index >= 4:
                    raise ValueError(
                        "Option number out of range. Please enter a number between 1 and 4."
                    )
                break
            except ValueError as e:
                print(e)

        question = Question(question_text, options, correct_option_index)
        self.add_question(question)

    def ask_question(self):
        current_question = self.questions[self.current_question_index]
        print(current_question)
        try:
            user_answer = int(input("Enter your answer (1-4): ")) - 1
            if current_question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(
                    f"Wrong. The correct answer was: {current_question.correct_option_index + 1}\n"
                )
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")
        finally:
            self.current_question_index += 1

    def is_quiz_over(self):
        return self.current_question_index >= len(self.questions)

    def get_score(self):
        return self.score
