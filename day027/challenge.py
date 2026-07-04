from tkinter import *

my_win = Tk()
my_win.title("Grid Challenge")
my_win.minsize(width=300, height=300)
my_win.maxsize(width=800, height=800)
my_win.config(padx=20, pady=50)
#padx and pady configures padding box in the window


my_label = Label()
my_label.config(text="My label in grid 0,0")
my_label.grid(column=0, row=0)

my_button1 = Button()
my_button1.config(text="Button in grid 1,1")
my_button1.grid(column=1, row=1)

my_button2 = Button()
my_button2.config(text="Button in grid 0,2")
my_button2.grid(column=2, row=0)

my_entry = Entry()
my_entry.config(width=10)
my_entry.grid(column=3, row=2)

my_win.mainloop()
