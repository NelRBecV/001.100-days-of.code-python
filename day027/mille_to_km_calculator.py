from tkinter import *


def clear_entry(event=None):
    e_num.delete(0, END)


def convert_m_km(event=None):
    miles = e_num.get()
    km = round(float(miles) * 1.609, 2)
    l_quantity['text'] = str(km)


FONT = ("Arial", 15, "bold")
window_converter = Tk()
window_converter.title("Mile to Km Converter")
window_converter.minsize(width=100, height=100)
window_converter.config(padx=20, pady=30)

e_num = Entry()
e_num.config(width=8, font=FONT)
e_num.insert(END, "0")
e_num.bind("<Button-1>", clear_entry)
e_num.bind("<Return>", convert_m_km)
e_num.grid(column=1, row=0)

l_miles = Label()
l_miles.config(text="Miles", font=FONT)
l_miles.grid(column=2, row=0)

l_equal = Label()
l_equal.config(text="is equal to", font=FONT)
l_equal.grid(column=0, row=1)

l_quantity= Label()
l_quantity.config(text="0", font=FONT)
l_quantity.grid(column=1, row=1)

l_km = Label()
l_km.config(text="Km", font=FONT)
l_km.grid(column=2, row=1)

b_calc = Button()
b_calc.config(text="Calculate", command=convert_m_km, font=FONT)
b_calc.grid(column=1, row=2)

window_converter.mainloop()
