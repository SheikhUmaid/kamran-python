from tkinter import *
import playsound


master = Tk()
master.geometry('500x500')

left_frame = LabelFrame(master, text = "your frame")

left_frame.pack(side = LEFT, fill = BOTH, expand = True)

right_frame = LabelFrame(master, text = "Client frame")

right_frame.pack(side = RIGHT, fill = BOTH, expand = True)

#  add one textbox under the both buttons

textbox = Entry(master)

textbox.pack(side = BOTTOM, fill = X)

def send_left():
    playsound.playsound('recv.mp3')
    Label(left_frame,text=textbox.get(), bg="red").pack(side=TOP, fill=X)

def send_right():
    playsound.playsound('recv.mp3')
    Label(right_frame,text=textbox.get(), bg="red").pack(side=TOP, fill=X)
# add one button on the bottom of the left frame

button = Button(left_frame, text = "Send", command = send_left)

button.pack(side = BOTTOM, fill = X)


# add one button on the bottom of the right frame

button = Button(right_frame, text = "Send", command = send_right)



button.pack(side = BOTTOM, fill = X)



mainloop()