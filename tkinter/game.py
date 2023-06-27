from tkinter import *



root = Tk()


play_frame = Frame(root)
play_frame.pack()



def play_forgeter():
    play_frame.pack_forget


Button(play_frame, text="Play").pack()




root.mainloop()