import tkinter as tk
from tkinter import messagebox
from tkinter import *
k=0


win=tk.Tk()

def fibo():
    messagebox.showinfo("addition series","adding the numbers")
    i=10
    j=20
    sum1=i+j
    print(sum1)
    string1= "ans is: " + str(sum1)
    l1.config(text=string1)
b1=Button(win,text="click to add", bg="red",fg="black",font=('Monotype Corsiva',20,'underline italic'),command=fibo)
b1.pack(expand=1,fill='y',side='top')
l1=Label(win,text="ans is:" ,bg="red",fg="black")
l1.pack(expand=0,fill='y',side='bottom')
        
win.mainloop()
