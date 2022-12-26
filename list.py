from tkinter import *
win=Tk()
win.title("Zalpars")
win.geometry("300x300")

def name_save():
    list_box.insert(END,name.get())

def delet():
    list_box.delete(0,END)

list_box=Listbox(win)
list_box.pack()

name=Entry(win)
name.pack()


Button(win,text="save",command=name_save).pack()
Button(win,text="delet",command=delet).pack()





win.mainloop()