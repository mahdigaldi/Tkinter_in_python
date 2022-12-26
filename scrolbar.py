from tkinter import *

win=Tk()
win.title("Eli$roghi")
win.geometry("200x200")

scrol=Scrollbar(win)
scrol.pack(side=RIGHT,fill=X)


list_box=Listbox(win)
list_box.pack(expand=True,fill=BOTH)

for i in range(2,100):
    list_box.insert(END,"num is : {}".format(i))

scrol.config(command=list_box.yview)


win.mainloop()