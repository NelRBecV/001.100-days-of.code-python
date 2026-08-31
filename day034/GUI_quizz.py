from tkinter import *
class QuizGUI(Tk):

    def __init__(self):
        super().__init__()
        FONT = [("Arial",22,"italic"), ("Arial",10,"bold")]
        BG = '#334b4e'
        self.title("Quizz Challenge")
        self.resizable(width=False, height=False)
        self.geometry("420x600")
        self.config(background=BG)
        # self.question = StringVar()
        self.answer = BooleanVar()
        self.score = IntVar()
        # self.question.set("Trivia's questions")
        self.score.set(0)
        self.i_true = PhotoImage(file="images/true.png")
        self.i_false = PhotoImage(file="images/false.png")
        self.c_elem = Canvas(height=300, width=345, bg='#ffffff')
        self.c_elem.grid(column=1, row=1, columnspan=2, padx=35, pady=40)
        self.text_trivia = self.c_elem.create_text(175,
                                                   150,
                                                   font=FONT[0],
                                                   fill=BG,
                                                   justify='center',
                                                   text="",
                                                   width=300)

        self.text_score = Label(font=FONT[1],
                                foreground='#ffffff',
                                text=f"Score: 0",
                                bg=BG)
        self.text_score.grid(column=2, row=0,sticky='e', pady=30, padx=30)


        self.b_true = Button(image=self.i_true,
                             highlightthickness=0,
                             relief='groove',
                             )
        self.b_true.grid(column=1, row=2, sticky='w',  padx=70)
        self.b_false = Button(image=self.i_false,
                              highlightthickness=0,
                              relief='groove'
                              )
        self.b_false.grid(column=1, row=2, columnspan=2,sticky='e', padx=70)







