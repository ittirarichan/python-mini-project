# question.py
class Question:
    def __init__(self, question_text, options, correct_option_index):
        self.question_text = question_text
        self.options = options
        self.correct_option_index = correct_option_index

    def check_answer(self, answer_index):
        return answer_index == self.correct_option_index

    def __str__(self):
        options_str = "\n".join([f"{i + 1}. {option}" for i, option in enumerate(self.options)])
        return f"{self.question_text}\n{options_str}"
