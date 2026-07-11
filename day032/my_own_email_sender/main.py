import datetime
import smtplib
import os
from random import randint
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv

with open("data/quotes.txt","r") as phrases:
    list_quotes = phrases.readlines()

WIDTH_TEXT_INPUT= 51
BG_COLOR = "#40f9ff"

def choose_server():
    serv_choice = s_email_servers.get()
    subject: str = e_subjet.get()
    message: str = t_message.get("1.0", "end-1c")  # watch the stack overflow screenshot in "Fireshot" folder
    dest: str = e_destination.get()
    user: str = ""
    password: str = ""
    serv: str = ""
    port: int = 0
    if serv_choice == "Gmail":
        user = os.getenv("USER_GMAIL")
        serv = os.getenv("SERV_GMAIL")
        password = os.getenv("PSWD_GMAIL")
        port = 587
    elif serv_choice == "Yahoo":
        user = os.getenv("USER_YAHOO")
        serv = os.getenv("SERV_YAHOO")
        password = os.getenv("PSWD_YAHOO")
        port = 587
    send_email(user,dest, subject, message)
    

def send_email(user, dest, subject, message):
    with smtplib.SMTP(serv, port) as serv_connection:
        serv_connection.ehlo("localhost")
        serv_connection.starttls()
        serv_connection.login(user=user, password=password)
        serv_connection.sendmail(from_addr=user, to_addrs=dest,
                                 msg=f"Subject: {subject}\nTo:{dest}\nFrom:{user}\n\n {message}")#
        

bwg = Tk()
bwg.title("Best Wishes Sender")
bwg.config(bg=BG_COLOR, padx=10, pady=20)

l_destination = Label(text="Destination: ", anchor="e", bg=BG_COLOR)
l_destination.grid(column=0, row=1, pady=5, sticky="e")

e_destination = Entry(width=WIDTH_TEXT_INPUT,)
e_destination.grid(column=1, row=1, sticky="w", pady=5,columnspan=2)

l_subjet = Label(text="Subject: ", anchor="w", bg=BG_COLOR)
l_subjet.grid(column=0, row=2, sticky="e", pady=5)

e_subjet = Entry(width=WIDTH_TEXT_INPUT)
e_subjet.grid(column=1, row=2, sticky="w", pady=5, columnspan=2)

l_message = Label(text="Message: ", anchor="w", bg=BG_COLOR)
l_message.grid(column=0, row=3, sticky="n,e")

t_message = Text(height=10, width=38)
t_message.grid(column=1, row=3, sticky="w", pady=5, columnspan=2)

sc_quotes = Scrollbar()
sc_quotes.grid(column=0, row=3, sticky="se,e")

sp_email_servers = Spinbox(values=EMAIL_SERVERS,state="readonly")
sp_email_servers.grid(column=1, row=4, sticky="w")

b_send = Button(text="Send", command=send_email)
b_send.place(x=343, y=235)

bwg.mainloop()

