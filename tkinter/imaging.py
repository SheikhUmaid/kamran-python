from tkinter import *

from PIL import ImageTk, Image
root = Tk()
img = Image.open("ico.png")
imgtk = ImageTk.PhotoImage(img)


Label(root, image=imgtk).grid(row=0,column=0, columnspan=3)
Button(root,text="<<").grid(row=1,column=0)
Button(root,text=">>").grid(row=1,column=2)
Button(root,text="exit", command = root.quit).grid(row=1,column=1)





root.mainloop()