from tkinter import *
import pyttsx3 as tts

a = tts.init()



win = Tk()


Label(win, text ="Enter yout name?").pack()

input_box = Entry(win)
input_box.pack()
def add():
    a  =eval(f"{input_box.get()}")

    Label(win, text=f"{a}").pack()
    # a.runAndWait()

Button(win, text="say", command=add).pack()


win.mainloop()