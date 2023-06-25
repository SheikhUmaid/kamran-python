from tkinter import *
from mic_working import listen


root = Tk()
root.title('mainlevel')
root.geometry("400x700")
toplevel = Toplevel()
toplevel.title("Toplevel")
toplevel.geometry("400x700")


def listen_update():
    text = listen()
    Label(toplevel, text=str(text),).pack()



Button(root, text="listen", command=listen_update).pack()
mainloop()