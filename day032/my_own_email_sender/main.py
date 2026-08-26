import smtplib
import os
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv()

with open("data/quotes.txt", "r") as phrases:
    list_quotes = phrases.readlines()

WIDTH_TEXT_INPUT = 51
BG_COLOR = "#88cc88"
EMAIL_SERVERS = ['Gmail', 'Yahoo']


def clear_screen():
    """Resets all form entries to blank."""
    e_subjet.delete(END)
    e_destination.delete(END)
    t_message.delete(END)
    e_subjet.focus_set()


def reformat_email_body(user) -> dict:
    """Reshapes text message to fit into email format."""
    subject: str = e_subjet.get()
    message: str = t_message.get("1.0",
                                 "end-1c")  # watch the stackoverflow screenshot in "Fireshot" folder for explanation
    dest: str = e_destination.get()
    return {"destination": dest, "message": f"Subject: {subject}\nTo:{dest}\nFrom:{user}\n\n {message}"}


def configure_smtp_server() -> dict:
    """Gets all necessary parameters to be able to send the recently created mail."""
    serv_choice = sp_email_servers.get().upper()
    if serv_choice:
        user = os.getenv(f"USER_{serv_choice}")
        serv = os.getenv(f"SERV_{serv_choice}")
        password = os.getenv(f"PSWD_{serv_choice}")
        port = os.getenv(f"PORT_{serv_choice}")
        return {"user": user, "password": password, "serv": serv, "port": port}
    

def send_email():
    """Sends the email by using the selected configuration."""
    server = configure_smtp_server()
    email_body = reformat_email_body(server['user'])
    if not server:
        messagebox.showerror("Select server", "No server chosen for sending.")
        return
    try:
        with smtplib.SMTP(server['serv'], server['port']) as serv_connection:
            serv_connection.ehlo("localhost")
            serv_connection.starttls()
            serv_connection.login(user=server['user'], password=server['password'])
            sender = serv_connection.sendmail(from_addr=server['user'], to_addrs=email_body['destination'],
                                              msg=email_body['message'])
            if not sender:
                messagebox.showinfo("Message sent", "Message was successfully sent.")
                clear_screen()
    except smtplib.SMTPException as e:
        messagebox.showwarning("Error", f"The program was unable to send email.\n{e}")


bwg = Tk()
bwg.title("E-mail sender App")
bwg.config(bg=BG_COLOR, padx=10, pady=20)

l_destination = Label(text="Destination: ", anchor="e", bg=BG_COLOR)
l_destination.grid(column=0, row=1, pady=5, sticky="e")

e_destination = Entry(width=WIDTH_TEXT_INPUT,)
e_destination.grid(column=1, row=1, sticky="w", pady=5, columnspan=2)

l_subjet = Label(text="Subject: ", anchor="w", bg=BG_COLOR)
l_subjet.grid(column=0, row=2, sticky="e", pady=5)

e_subjet = Entry(width=WIDTH_TEXT_INPUT)
e_subjet.grid(column=1, row=2, sticky="w", pady=5, columnspan=2)

l_message = Label(text="Message: ", anchor="w", bg=BG_COLOR)
l_message.grid(column=0, row=3, sticky="n,e")

t_message = Text(height=10, width=38)
t_message.grid(column=1, row=3, sticky="w", pady=5, columnspan=2)

sp_email_servers = Spinbox(values=EMAIL_SERVERS, state="readonly")
sp_email_servers.grid(column=1, row=4, sticky="w")

b_send = Button(text="Send", command=send_email)
b_send.place(x=343, y=235)

bwg.mainloop()
