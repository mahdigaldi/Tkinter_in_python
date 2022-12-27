from tkinter import *
win=Tk()
win.geometry("500x230")
cw=Canvas(win)
cw.pack()

pane1=PanedWindow(win,bd=4,bg="red")
pane1.pack(fill=BOTH,expand=True)

lab=Label(pane1,text="panel1",font="tahoma 20 ")
pane1.add(lab)

pane2=PanedWindow(win,bg="green",orient=VERTICAL)
pane1.add(pane2)

lab2=Label(pane2,text="panel2",font="aria 32")
pane2.add(lab2)
#pane2.add(pane1)



# lab3=PhotoImage(file="1.png")
# img=cw.create_image(200,300,Image=lab3)
# pane2.add(lab3)
# 



win.mainloop()