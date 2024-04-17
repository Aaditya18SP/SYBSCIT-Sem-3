import tkinter
from tkinter import *
from tkinter import Label
win=tkinter.Tk()

def sel():
    string1="Value is:"+ str(var.get())
    L1.config(text=string1)
var=DoubleVar()
S1=Spinbox(win,from_=0,to=10)
S1.pack()

L1=Label(win,text="Value is:")
L1.pack()
B1=Button(win,text="click",command=sel)
B1.pack()


win.mainloop()
