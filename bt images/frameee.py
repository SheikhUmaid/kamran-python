from tkinter import *


master = Tk()

img = PhotoImage(file = "btn-img.png")

resized = img.subsample(5,5)


frame1 = LabelFrame(master, text="This is frame 1",bg = "green")
frame1.grid(row=0, column=0)
# frame2 = Frame(master)
# frame2.pack()
entry = Entry(frame1, show="." )


Button(frame1, image=resized, text = "Click Me", compound=RIGHT, command=lambda: print(entry.get())).pack(padx=20, pady=20)
entry.pack(padx=20, pady=20)
mainloop()