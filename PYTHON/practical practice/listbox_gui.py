import tkinter as tk
from tkinter import Listbox
from tkinter import *


win=tk.Tk()
label1=Label(win,text="list 2").pack()
L2=Listbox(win,selectmode="browse")
L2.pack()
def ins():
    
    L2.delete(0,END)
    tuple1=L1.curselection()
    for i in tuple1:
        L2.insert(END,L1.get(i))
def dele():
    tuple2=L2.curselection()
    for i in tuple2:
        L2.delete(i,END)

label=Label(win,text="list 1").pack()
L1=Listbox(win,selectmode="extended",fg="black")
L1.pack()
L1.insert(1,'python')
L1.insert(1,'c++')
L1.insert(1,'c')
L1.insert(1,'java')
b1=Button(win,text="Insert",relief="raised",command=ins).pack()
b2=Button(win,text="Delete",relief="raised",command=dele).pack()
win.mainloop()
