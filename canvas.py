from tkinter import *
win=Tk()
win.geometry("500x420")

cw=Canvas(win,width=200,height=320)
cw.pack()

cw.create_line(10,20,10,140)
cw.create_oval(220,20,340,100,fill="#256585",dash=(4,2))
cw.create_rectangle(100,20,200,100 , fill="#958545")
cw.create_text(100,50,text="heloo",font="tahoma 20 bold",fill="#139574")

cw.create_polygon(10,120,10,180,80,180,fill="blue",outline="red",width=5)

img=PhotoImage(file='1.png')
cw.create_image(200,350,image=img)


win.mainloop()