import tkinter
from tkinter import Tk,  Entry


root = Tk()



root.title("Chatboot")
root.geometry("300x650")
root.minsize(width=200, height=250)

def button_click():
    label.config(text="your name is "+ e.get())

label = tkinter.Label(root, text="Willkommen!")
label.pack(pady=10)
e = Entry(root, width=20)
e.pack()
button = tkinter.Button(root, text="Klick mich", command=button_click)
button.pack(pady=10)


root.mainloop()
