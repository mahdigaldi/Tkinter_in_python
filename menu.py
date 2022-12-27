
from tkinter import *
import sys
win=Tk()
win.title("Zalpars")


men=Menu(win)


men2=Menu(men,tearoff=0)
men2.add_command(label="file")
men2.add_command(label="exit",command=sys.exit)


men.add_cascade(label="open",menu=men2)


win.config(menu=men)
win.geometry("500x500")
win.mainloop()