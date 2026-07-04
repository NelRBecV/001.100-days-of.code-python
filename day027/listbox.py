import tkinter

root = tkinter.Tk()
label = tkinter.Label(root)
listbox = tkinter.Listbox(root)
label.pack(side="bottom")
listbox.pack(side="top", expand=True)
listbox.insert("end", "one", "two", "three", "four", "five")


def display_status(event):
    index = event.widget.curselection()[0]
    data = event.widget.get(index)
    label.config(text=data)
    

listbox.bind("<<ListboxSelect>>", display_status)

root.mainloop()
