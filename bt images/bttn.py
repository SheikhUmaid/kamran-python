from tkinter import *


master = Tk()
master.geometry("700x700")
img = PhotoImage(file = "btn-img.png")



resized = img.subsample(5,5)
Button(master, image=resized, text = "Click Me", compound=RIGHT, height=150).pack()
mainloop()