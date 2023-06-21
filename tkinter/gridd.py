from tkinter import *
from PIL import ImageTk,Image 


root = Tk()
root.title("Faster")
root.iconbitmap("icon.ico")


button = Button(root, text =" click Me ")
button2 = Button(root, text =" click Me 2 ")
label = Label(root, text="                                ")
button.grid(row=0, column=0)
label.grid(row=0,column= 1)
button2.grid(row=0 ,column=2)

# button2.grid(row=0 ,column=1)








root.mainloop()