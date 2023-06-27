from tkinter import *


master = Tk()

img = PhotoImage(file = "btn-img.png")

resized = img.subsample(5,5)


def erase(w):
    w.pack_forget()

btn1 = Button(master, text="HEllo")
btn1.pack()

btn = Button(master, text = "eraseme", command=lambda : erase(btn))
btn.pack()


mainloop()