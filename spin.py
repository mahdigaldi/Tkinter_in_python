from tkinter import *

win=Tk()
win.title("Eli$roghi")
win.geometry("550x550")

spin=Spinbox(win,from_=1,to=4)
spin.pack()

def click():
    lable1.config(text=spin.get())
    lable1.pack()
lable1=Label(win,text="",fg="#995285",bg="#000022",font="titr")

Button(win,text="کلیک کن روی من",command=click).pack()

win.mainloop()