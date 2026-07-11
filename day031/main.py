from random import *
import pandas
from tkinter import *
from tkinter import messagebox
import json

BACKGROUND_COLOR: str = "#b1ddc6"
FONT_1: tuple = ("Arial", 30, "italic")
FONT_2: tuple = ("Arial", 80, "bold")


def arrange_cards_info(data):
    english: list = data['English'].tolist()
    french: list = data['French'].tolist()
    u_words: list = [{"French": french[i], "English": english[i]} for i in range(len(english))] 
    return u_words


def generate_words_list():
    test_words = pandas.read_csv("data/few_french_words.csv")
    words: list = []

    try:
        with open("missing_words.json") as missing_words:
            words = json.load(missing_words)
    except FileNotFoundError:
        words = arrange_cards_info(test_words)
    else:
        if len(words) == 0:
            win.withdraw()  # Hide the current window
            new_lap: bool = messagebox.askyesno(title="Start Over",
                                                message="You've learned all standard words. Do you wanna start over?")
            if new_lap:
                words = arrange_cards_info(test_words)
                win.deiconify()  # shows the hidden window again
            else:
                messagebox.showinfo("Finish", "Program closed")
                win.destroy()
    finally:
        shuffle(words)
        return words


def start_showing():
    global ind, word_list

    b_wrong.config(state=DISABLED, highlightthickness=0, highlightcolor=BACKGROUND_COLOR)
    b_right.config(state=DISABLED, highlightthickness=0, highlightcolor=BACKGROUND_COLOR)

    if ind > len(word_list) - 1:
        messagebox.showinfo("Finish", "Word list ended")
        win.destroy()

    win.after(100, generate_card_word, ind, word_list)


def generate_card_word(index, my_list):
    title: str = "French"
    word, answer = my_list[index].values()
    flash_card.itemconfig(lang_title, text=title, fill="black")
    flash_card.itemconfig(lang_word, text=word, fill="black")
    flash_card.itemconfig(bg_img, image=front_card_bg)
    win.after(3000, show_answer, answer)


def show_answer(answer_word):
    b_wrong.config(state=NORMAL, highlightthickness=0, highlightcolor=BACKGROUND_COLOR)
    b_right.config(state=NORMAL, highlightthickness=0, highlightcolor=BACKGROUND_COLOR)
    title = "English"
    flash_card.itemconfig(lang_title, text=title, fill="white")
    flash_card.itemconfig(lang_word, text=answer_word, fill="white")
    flash_card.itemconfig(bg_img, image=back_card_bg)


def remember_word(remember: bool = False):
    global ind, reminder, word_list

    if not remember:
        reminder.remove(word_list[ind])

    with open("missing_words.json", "w") as lost_words:
        json.dump(reminder, lost_words, indent=4)
        lost_words.close()

    ind += 1
    start_showing()


def right_words():
    remember_word()


def wrong_words():
    remember_word(True)


win = Tk()
win.title("                                                                             "
          "                                  Word Reminder")
ind = 0
right = 0
word_list = generate_words_list()
reminder = word_list.copy()

win.config(width=1000, height=1000, padx=20, pady=10, bg=BACKGROUND_COLOR)
flash_card = Canvas(height=550, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_bg = PhotoImage(file="images/card_front.png")
back_card_bg = PhotoImage(file="images/card_back.png")
right_bg = PhotoImage(file="images/right.png")
wrong_bg = PhotoImage(file="images/wrong.png")

bg_img = flash_card.create_image(410, 280, image=front_card_bg)
lang_title = flash_card.create_text(400, 200, text="", fill="black", justify="center", font=FONT_1)
lang_word = flash_card.create_text(400, 300, text="", fill="black", justify="center", font=FONT_2)
flash_card.grid(column=0, row=0, columnspan=3, rowspan=2, padx=5, pady=0)

b_right = Button(image=right_bg, width=100, anchor="n", highlightthickness=0, command=right_words,
                 highlightcolor=BACKGROUND_COLOR, relief="flat", bg=BACKGROUND_COLOR)
b_right.grid(column=0, row=2)

b_wrong = Button(image=wrong_bg, width=100, anchor="n", highlightthickness=0, command=wrong_words,
                 highlightbackground=BACKGROUND_COLOR, relief="flat", bg=BACKGROUND_COLOR)
b_wrong.grid(column=2, row=2)

start_showing()

win.mainloop()
