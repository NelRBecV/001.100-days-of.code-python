class QuizBrain:
    def __init__(self, quiz_list):
        self.question_number = 0
        self.question_list = quiz_list
        self.score = 0

    # TODO-3: checking if we're the end of the quiz
    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    # TODO-1: Asking the questions
    def next_question(self):
        question_c = self.question_list[self.question_number]
        self.question_number += 1
        show_question = input(f"Q.{self.question_number}: {question_c.text} (True/False)?: ").capitalize()
        self.check_answer(show_question, question_c.answer)

    # TODO-2: Checking if the answer is correct
    def check_answer(self, answer, r_answer):
        if answer == r_answer:
            self.score += 1
            print(f"That's right.")
        else:
            print(f"That's wrong.")

        print(f"The correct answer is '{r_answer}'")
        print(f"Your score is: {self.score}/{self.question_number}")
