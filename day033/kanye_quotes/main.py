from tkinter import *
import requests


def get_quote():
    #creates a connection between the "Kanye rest" api and our program
    data_bank = requests.get("https://api.kanye.rest")
  
    # Raises every single error that request variable (data_bank) can get
    data_bank.raise_for_status()
    quotes = data_bank.json()
    q = len(f"{quotes['quote']}".split())
  
    if q > 25:
        font_conf = ("Arial",18, "bold")
    elif q >= 22:
        font_conf = ("Arial", 20, "bold")
    else:
        font_conf = ("Arial",21, "bold")

    image.itemconfig(quote_text, text=quotes['quote'], font=font_conf)

win = Tk()
win.title("Kanye's Quotes")
win.config(height=600, width=500)

b_ground = PhotoImage(file="background.png")
kanye_photo = PhotoImage(file="kanye.png")
image = Canvas(height=570, width=400)
quote_bg = image.create_image(200,225, image=b_ground)
quote_text = image.create_text(200, 210, text="Kanye's quotes go here", fill="white", font=("Arial", 22,"bold"),
                               width=280, justify="center")

image.grid(column=0, row=0, pady=10)
b_kanye = Button(image=kanye_photo, command=get_quote, height=140, width=100, relief="groove", highlightthickness=0,
                 borderwidth=0)
b_kanye.grid(column=0, row=0, rowspan=2, sticky="s", pady=10)
win.mainloop()
