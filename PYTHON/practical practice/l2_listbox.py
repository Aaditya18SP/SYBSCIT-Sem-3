from tkinter import *
import tkinter
top = Tk()
Lb2 = Listbox(top)
Lb2.pack()
def CurSelet():
    Lb2.delete(0,END)
    value=Lb1.curselection()
    for items in value:
        Lb2.insert(END,Lb1.get(items))
def deleteselection():
    value=Lb2.curselection()
    for items in value:
        Lb2.delete(items,END)
L=Label(top,text="List Items are as follows",font=("Monotype Corsiva",15)).pack()
Lb1 = Listbox(top,selectmode="multiple")
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()
b=Button(top,text="Insert",command=CurSelet).pack()
b1=Button(top,text="Delete",command=deleteselection).pack()
top.mainloop()
