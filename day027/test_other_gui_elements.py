from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def actions():
    print("Do something")
    

#calls actions() when pressed
button= Button(text="Click Me", command=actions)
button.pack()

#Entries
entry = Entry(width=30)

#Add some text to begin with
entry.insert(END, "Some text to begin with")

#Get text in entry
print(entry.get())
entry.pack()

#Text
text = Text(width=25, height=3)
#puts cursor in textbox
text.focus()
#Add some text to begin with
text.insert(END, "Example of multi-line text entry")
#Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value from spinbox
    print(spinbox.get())
    

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale
#Called with current scale value
def scale_used(value):
    print(value)
    

scale = Scale(from_= 0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if in button checked. Otherwise 0
    print(checked_state.get())
    
    
#Variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is's on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
    

#variable that holds on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    #Gets the current selection from listbox
     print(listbox.get(listbox.curselection()))
     

listbox = Listbox(window, height=4)
fruits: list = ['Apple', 'Pear','Orange', 'Banana']

for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
