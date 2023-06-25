from tkinter import (Tk,Entry,Button, END, messagebox) 
root=Tk()

entry=Entry(root,font=('times 50'))
entry.grid(column=0, row=0, columnspan=4)

root.title("Calculator")


def all_number(number):
    entry.insert(END,number)

def Evaluate():
    try:
        sol=eval(entry.get())

        entry.delete(0,END) 
        entry.insert(0,sol)
    except ZeroDivisionError:
        entry.delete(0,END) 
        entry.insert(0,"Can't divide with zero")
    except SyntaxError:
        entry.delete(0,END) 
        entry.insert(0,"Enter Valid Expression")


def clear():
    entry.delete(0,END)


def exit():
    message=messagebox.askokcancel("Warning", "Do you want to Exit") 
    if message ==True:
        root.quit()
    else:
        pass


def clear():
    entry.delete(0,END)

def clear1():
    entry.delete(len(entry.get())-1)



button0=Button(root,text="0",padx=30, pady=30,bg="#faedee",command=lambda:all_number("0"))
button2=Button(root,text="2",padx=30, pady=30,bg="#faedee",command=lambda:all_number("2"))
button1=Button(root,text="1",padx=30, pady=30,bg="#faedee",command=lambda:all_number("1"))
button3=Button(root,text="3",padx=30, pady=30,bg="#faedee",command=lambda:all_number("3"))
button4=Button(root,text="4",padx=30, pady=30,bg="#faedee",command=lambda:all_number("4"))
button5=Button(root,text="5",padx=30, pady=30,bg="#faedee",command=lambda:all_number("5"))
button6=Button(root,text="6",padx=30, pady=30,bg="#faedee",command=lambda:all_number("6"))
button7=Button(root,text="7",padx=30, pady=30,bg="#faedee",command=lambda:all_number("7"))
button8=Button(root,text="8",padx=30, pady=30,bg="#faedee",command=lambda:all_number("8"))
button9=Button(root,text="9",padx=30, pady=30,bg="#faedee",command=lambda:all_number("9"))



button_add=Button(root,text="+",padx=30, pady=30,bg="#1df2d9",command=lambda:all_number("+"))
button_sub=Button(root,text="-",padx=30, pady=30,bg="#f2d61d",command=lambda:all_number("-"))
button_mult=Button(root,text="X",padx=30, pady=30,bg="#f21d41",command=lambda:all_number("*"))
button_div=Button(root,text="/",padx=30, pady=30,bg="#ff0a0a",command=lambda:all_number("/"))
button_power=Button(root,text="Power",padx=30, pady=30,bg="#6721ff",command=lambda:all_number("**"))
button_point=Button(root,text="!point",padx=30, pady=30,command=lambda:all_number("//"),bg='#0ffc03')


button_equal=Button(root,text="=",padx=30, pady=30,command=Evaluate,bg="#294bf2")


button_quit=Button(root,text="QUIT",command=exit,padx=30, pady=30,bg="#fc6603")




button_clear=Button(root,text="clear",command=clear,padx=30, pady=30,bg='#8803fc')


button_clear1=Button(root,text="Delete",command=clear1,padx=30, pady=30,bg='#f20505')




button7.grid(row=1,column=0)
button4.grid(row=2,column=0)
button1.grid(row=3,column=0)

button8.grid(row=1,column=1)
button5.grid(row=2,column=1)
button2.grid(row=3,column=1)

button3.grid(row=1,column=2)
button6.grid(row=2,column=2)
button9.grid(row=3,column=2)

button0.grid(row=4,column=1)


button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mult.grid(row=3,column=3)
button_div.grid(row=4,column=3)
button_power.grid(row=5,column=3)
button_point.grid(row=5,column=2)



button_equal.grid(row=4,column=2)

button_quit.grid(row=4,column=0)


button_clear.grid(row=5,column=0)

button_clear1.grid(row=5,column=1)
















root.mainloop()