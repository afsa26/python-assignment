from tkinter import *

from tkinter import *

screen =Tk()
screen.geometry("500X600")
var_e1 =StringVar()
var_r1 =StringVar()

def myfun():
    firstname = var_e1.get()
    var_r1.set(firstname)

lbl = Label(screen,text="Enter your First Name:")
lbl.place(x=10,y=10)
e1 = Entry(screen,width=20,textvariable=var_e1)
e1.place(x=120,y=10)
lbl = Label(screen,text="Enter your Last Name:")
lbl.place(x=10,y=20)
e1.Entry(screen,width=20,textvariable=var_e1)
e1.place(x=120,y=10)
lbl = Label(screen,text="Enter Gender:")
lbl.place(x=10,y=20)
e1.Entry(screen,width=20,textvariable=var_e1)
e1.place(x=120,y=10)
lbl = Label(screen,text="Enter your Age:")
lbl.place(x=10,y=20)
e1.Entry(screen,width=20,textvariable=var_e1)
e1.place(x=120,y=10)
lbl = Label(screen,text="Enter Vaccination Dose:")
lbl.place(x=10,y=20)
e1.Entry(screen,width=20,textvariable=var_e1)
e1.place(x=120,y=10)




Tk.mainloop()