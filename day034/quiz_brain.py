
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
        return question_c

    # TODO-2: Checking if the answer is correct
    def check_answer(self, answer, r_answer):
        if answer == r_answer:
            return True
        else:
            return False




