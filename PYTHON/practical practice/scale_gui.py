import tkinter
from tkinter import *
from tkinter import Label
win=tkinter.Tk()

var=DoubleVar()
S1=Scale(win,variable=var,orient=HORIZONTAL,troughcolor="green",from_=0,to_=100,tickinterval=25)
S1.pack()
def sel():
    string1="value is:" +str(var.get())
    L1.config(text=string1)



L1=Label(win,text="value is:")
L1.pack()


B1=Button(win,text="Get value",command=sel).pack()

win.mainloop()
