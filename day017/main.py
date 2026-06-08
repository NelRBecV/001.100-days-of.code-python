from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []
for i in range(len(question_data)):
    question_game = Question(question_data[i]['question'], question_data[i]['correct_answer'])
    question_bank.append(question_game)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print("You completed the quiz")
print(f"Your final score was: {quiz.score} right answers"
      f" over {quiz.question_number} questions")
