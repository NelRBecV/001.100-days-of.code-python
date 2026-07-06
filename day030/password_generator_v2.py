from tkinter import *
from tkinter import messagebox
from random import randint
import json

ENTRY_FONT: tuple = ("Arial", 10, "normal")
BACKGROUND_COLOR: str = "#fefff8"
BORDER: int = 2

# -------------------------------- PASWORD GENERATOR ----------------------------------------#
ALPHABETH: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z',
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS: list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS: list = ["°", "!", '"', "#", "$", "%", "&", "/", "(", ")", "=", "?", "¡", "¨", "+", "}", "{", "-", ".", ","]
CHARACTERS: list = ALPHABETH + NUMBERS + SYMBOLS


def generate_password():
    """creates a random password"""

    pwrd: str = ""
    e_password.delete(0, END)
    for i in range(20):
        pwrd += CHARACTERS[randint(0, 81)]
    e_password.insert(END, pwrd)


# ---------------------------------- SAVE PASSWORD ------------------------------------------#
def verify_input():
    """checks if all fields are filled by user"""

    user_web: str = e_website.get()
    user_email: str = e_email.get()
    user_pass: str = e_password.get()
    if user_web == "" or user_email == "" or user_pass == "":
        messagebox.showwarning("Missing Data", "Don't leave white blanks")
    else:
        m_confirm: bool = messagebox.askyesno(title=f"{user_web}", message=f"{user_email}\n{user_pass}\nIs this ok?")
        if m_confirm:
            save_data(user_web, user_email, user_pass)
        else:
            messagebox.showinfo("Info", "Data not saved")
        new_entry()


def save_data(user, email, psswd):
    """storages user inorfmation into a database"""

    savedata: dict = {f"{user}": {"e-mail": f"{email}", "password": f"{psswd}"}}
    my_record: str = ""
    userdata: str = ""
    try:
        with open("data.json", "r") as my_data:
            my_records = json.load(my_data)
            my_records.update(savedata)
            write_data(my_records)
    except FileNotFoundError:
        write_data(savedata)
    finally:
        messagebox.showinfo("Save", "Data saved successfully")


def write_data(save):
    """saves user data in a file"""
    userdata = open("data.json", "w")
    json.dump(save, userdata, indent=4)
    userdata.close()


def new_entry():
    """clean all entries"""

    e_email.delete(0, END)
    e_website.delete(0, END)
    e_password.delete(0, END)
    e_website.focus_set()


def search_data():
    """
       looks for a user into the main database.

       The program retrieve info related to him/her if the record does exist,
       otherwise it will raise an exception.
    """

    record: str = e_website.get()
    found: dict = {}
    try:
        with open("data.json") as file_search:
            search = json.load(file_search)
            found = search[record]
            if not found:
                raise Exception

    except FileNotFoundError:
        messagebox.showinfo("Search", "File record doesn't exist")
    except Exception:
        messagebox.showinfo("Search", "Record not found")
    else:
        messagebox.showinfo("Search", f"{record}:\n "
                                      f"E-mail:{found['e-mail']}\n"
                                      f"Password:{found['password']}")
    finally:
        e_email.delete(0, END)
        e_password.delete(0, END)

# ------------------------------------- UI SETUP --------------------------------------------#
main_window = Tk()
main_window.title("Password Manager")
main_window.config(background=BACKGROUND_COLOR, width=200, height=200, padx=40, pady=40)

bg_pict = Canvas(background=BACKGROUND_COLOR, width=200, height=180, highlightthickness=0)
bg_img = PhotoImage(file="logo.png")
bg_pict.create_image(60, 80, image=bg_img)
bg_pict.grid(column=1, row=1, columnspan=2)

l_website = Label(text="Website: ", background=BACKGROUND_COLOR)
l_website.grid(column=0, row=2, padx=5, pady=3)

e_website = Entry(width=20, font=ENTRY_FONT, border=BORDER)
e_website.grid(column=1, row=2, pady=5, padx=3)

b_search = Button(width=16, text="Search", command=search_data)
b_search.grid(column=2, row=2, pady=5, sticky="w")

l_email = Label(text="E-mail/username: ", background=BACKGROUND_COLOR)
l_email.grid(column=0, row=3, padx=5, pady=2)

e_email = Entry(width=38, font=ENTRY_FONT, border=BORDER)
e_email.grid(column=1, row=3, padx=5, pady=3, columnspan=2)

l_password = Label(text="Password: ", background=BACKGROUND_COLOR)
l_password.grid(column=0, row=4, padx=5, pady=2)

e_password = Entry(width=20, justify="left", font=ENTRY_FONT, border=BORDER)
e_password.grid(column=1, row=4, padx=0, pady=5)  # place(x=118, y=240, height=25)

b_gen_pass = Button(text="Generate Password", justify="right", width=16, command=generate_password)
b_gen_pass.grid(column=2, row=4, pady=5, sticky="w")  # place(x=280, y=238, height=25)#

b_add = Button(text="add", width=38, command=verify_input)
b_add.grid(column=1, row=5, padx=3, pady=8, columnspan=2)

main_window.mainloop()
