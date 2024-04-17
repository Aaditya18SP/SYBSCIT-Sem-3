import tkinter
from tkinter import *
from tkinter import Label
win=tkinter.Tk()

S1=Scrollbar(win,orient=VERTICAL)
S1.pack(side="right",fill="y")

L1=Listbox(win,selectmode="multiple",yscrollcommand=S1.set)
for i in range(20):
    L1.insert(END,i)
L1.pack(side="left")
S1.config(command=L1.yview)

win.mainloop()
