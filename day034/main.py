import html
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from GUI_quizz import QuizGUI

front_screen = QuizGUI()
quiz = QuizBrain(question_data)
texto = front_screen.text_trivia
marco = front_screen.c_elem
points = front_screen.text_score
def start_game():
    marco.config(bg='#ffffff')
    marco.itemconfig(texto, fill='#334b4e')
    if quiz.still_has_questions():
        r_question = quiz.next_question()
        q = html.unescape(r_question['question'])
        front_screen.answer.set(r_question['answer'])
        front_screen.c_elem.itemconfig(texto, text=q)
    else:
        message=f"The Quiz has ended.\n Your final score is:\n {front_screen.score.get()} points"
        front_screen.c_elem.config(bg='#ffffff')
        front_screen.c_elem.itemconfig(texto,text=message, fill='#334b4e')
        front_screen.b_true.config(state="disabled")
        front_screen.b_false.config(state="disabled")

def true_answer():
    answer = True
    is_correct(answer)

def false_answer():
    answer = False
    is_correct(answer)

def is_correct(answer):
    an = front_screen.answer.get()
    if quiz.check_answer(answer,an):
        score = front_screen.score.get()
        score += 1
        front_screen.score.set(score)
        front_screen.c_elem.config(bg='#00ff00')
        front_screen.text_score.config(text=f"Score: {front_screen.score.get()}")
        front_screen.c_elem.itemconfig(texto, fill='#000000')
    else:
        front_screen.c_elem.config(bg='#ff0000')
        front_screen.c_elem.itemconfig(texto, fill='#ffffff')

    front_screen.after(1000, start_game)

start_game()
front_screen.b_true.config(command=true_answer)
front_screen.b_false.config(command=false_answer)
front_screen.mainloop()