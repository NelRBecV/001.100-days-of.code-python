import tkinter


# add actions to window objects
def button_clicked():
    message = tkinter.Message()
    message.config(text="You got clicked me", anchor="ne")
    message.pack()

def show_text():
    text: str = my_text.get()
    if not text:
        text = "nothing"
    print(f"You wrote {text}")
    my_text.set("")


def change_label():
    my_label["text"] = "I changed"
    
    
#Create a window
my_window = tkinter.Tk()
my_window.minsize(200,200)
my_window.maxsize(700,700)

#Create window elements
my_label = tkinter.Label(text="My first Label", justify="center", font=("Arial", 20, "bold") )
my_label.pack()

my_button = tkinter.Button(text="Bye, Bye", command=my_window.destroy)
my_button.pack()

my_checkbutton = tkinter.Checkbutton(text=" check button", compound="left")
my_checkbutton.pack()

my_window.title("My First window in Python")
label2 = tkinter.Label()
label2["text"] = "Configuring Label 2 with a Dictionary index"

label3 = tkinter.Label()
label3.config(text="Configuring Label 3 with a function")

label2.pack()
label3.pack()

message_button = tkinter.Button()
message_button.config(text= "click me", command=change_label)
message_button.pack()

my_text = tkinter.StringVar()
text_input = tkinter.Entry(textvariable=my_text)
text_input.config(width= 8)
text_input.pack()
text_button = tkinter.Button()
text_button.config(text= "Show", command=show_text)
text_button.pack()

my_window.mainloop()
