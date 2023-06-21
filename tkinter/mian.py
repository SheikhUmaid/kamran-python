from tkinter import (Tk, Label, Button, Entry)
import pyttsx3 as tts

engine = tts.init()


root = Tk()
root.title("Game")
def say():
    engine.say("Clicked")
    engine.runAndWait()


Button(root, text="Click me", command=say, bg="#220000", fg = "white", padx=50, pady=50).pack()
Button(root, text="Click me", command=say, bg="#440000", fg = "white").pack()


# hello_world_text.pack()

root.mainloop()