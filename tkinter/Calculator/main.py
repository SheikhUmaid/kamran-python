from tkinter import (Tk,Entry,Button, END, messagebox)


root = Tk()
root.title("Calculator")

entry_box = Entry(root, font=('times 50'))
entry_box.grid(column=0, row=0, columnspan=4)




def add_to_entry(number):
    entry_box.insert(END, number)



def clear():
    entry_box.delete(0, END)



def Evaluate():
    solution = eval(entry_box.get())
    entry_box.delete(0, END)
    entry_box.insert(0,solution)


def exit():

    message = messagebox.askokcancel("Warning", "Do you want to Exit")
    if message == True:
        root.quit()
    else:
        pass

#defining Buttons
button0 = Button(root, text="0", padx=20, pady=20, command=lambda : add_to_entry('0'))
button1 = Button(root, text="1", padx=20, pady=20, command=lambda : add_to_entry('1'))
button2 = Button(root, text="2", padx=20, pady=20, command=lambda : add_to_entry('2'))
button3 = Button(root, text="3", padx=20, pady=20, command=lambda : add_to_entry('3'))
button4 = Button(root, text="4", padx=20, pady=20, command=lambda : add_to_entry('4'))
button5 = Button(root, text="5", padx=20, pady=20, command=lambda : add_to_entry('5'))
button6 = Button(root, text="6", padx=20, pady=20, command=lambda : add_to_entry('6'))
button7 = Button(root, text="7", padx=20, pady=20, command=lambda : add_to_entry('7'))
button8 = Button(root, text="8", padx=20, pady=20, command=lambda : add_to_entry('8'))
button9 = Button(root, text="9", padx=20, pady=20, command=lambda : add_to_entry('9'))


button_add = Button(root, text = '+',padx=20, pady=20, command=lambda : add_to_entry('+'))
button_sub = Button(root, text = '-',padx=20, pady=20, command=lambda : add_to_entry('-'))
button_mult = Button(root, text = 'x',padx=20, pady=20, command=lambda : add_to_entry('X'))



button_equal = Button(root, text= " = ", pady=20, padx=40 , bg = 'green', command=Evaluate)
button_clear = Button(root, text= " clear ", pady=20, padx=20 , bg = 'red', command= clear)

button_quit = Button(root , text = 'Quit', pady=20, padx=100 , command=exit)

#gridding buttons
button9.grid(row=1, column=2)
button8.grid(row=1, column=1)
button7.grid(row=1, column=0)
button_add.grid(row=1, column=3)

button6.grid(row=2, column=2)
button5.grid(row=2, column=1)
button4.grid(row=2, column=0)
button_sub.grid(row=2, column=3)


button3.grid(row=3, column=2)
button2.grid(row=3, column=1)
button1.grid(row=3, column=0)
button_mult.grid(row=3, column=3)


button0.grid(row=4, column= 1)
button_equal.grid(row=4, column= 2, columnspan= 2)
button_clear.grid(row=4, column=0)



button_quit.grid(row=5, column=0, columnspan=4)



root.mainloop()