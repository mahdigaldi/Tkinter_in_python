
from tkinter import *
from tkinter import messagebox
import sys
win=Tk()
win.title("Zalpars")

def showeror():
    messagebox.askquestion("exit","exit")





men=Menu(win)


men2=Menu(men,tearoff=0)
men2.add_command(label="file")
men2.add_command(label="exit",command=sys.exit)


men.add_cascade(label="open",menu=men2)


d1=Button(win,text="show eror",command=showeror)
d1.pack()


win.config(menu=men)
win.geometry("500x500")
win.mainloop()