'''''
GUI
'''''
from logging import exception
from multiprocessing import connection
from sqlite3 import Cursor
from tkinter import*
import tkinter.messagebox as msg
import mysql.connector

def clear_fields():
    entry_fname.delete(0,"end")
    entry_lname.delete(0,"end")
    entry_email.delete(0,"end")
    entry_phone.delete(0,"end")

def  create_connection():
        host="localhost",
    return mysql.connector.connect(
        password="",
        user="root",
        database="students"
    )
def insert_data():
    if entry_fname.get()==""or entry_lname.get()=="" or entry_email.get()=="" or entry_phone.get():
    msg.showerror("Missing fields","All fields but id are mandatory")    
    clear_fields()
else:
    try:
        connection=create_connection()
        Cursor=connection.Cursor
        query="Insret into classmates(fname,lname,email,phone)values(%s,%s,%s,%s)"
        args=(entry_fname.get(),entry_lname.get(),entry_email.get(),entry_phone.get())
        Cursor.execute(query,args)
        connection.commit()
        connection.close()
        msg.showinfo("success","Data insreted successfully")
        clear_fields()
    except exception as e:
        print(f"\n\n\n{e}\n\n\n")
        msg.showerror("Error","Something went wrong")

root=Tk()
root.title("My first TK App")
root.geometry("500x500")
root.resizable(False,False)
#label id
label_id=Label(root,text="ID  :")
label_id.place(x=50,y=50)

#Entry Id
entry_id=Entry(root)
entry_id.place(x=130,y=50)

#Label first name

label_fname=Label(root,text="First Name :")
label_fname.place(x=50,y=90)

#entry firstname
entry_fname=Entry(root)
entry_fname.place(x=130,y=90)

#label lastname
label_lname=Label(root,text="Last Name :")
label_lname.place(x=50,y=130)

#entry lastname
entry_lname=Entry(root)
entry_lname.place(x=130,y=130)

#labe Phone
label_phone=Label(root,text="Phone NO:")
label_phone.place(x=50,y=160)

#entry phone no
entry_phone=Entry(root)
entry_phone.place(x=130,y=160)

#label email
label_email=Label(root,text="Email :")
label_email.place(x=50,y=210)

#entry email
entry_email=Entry(root)
entry_email.place(x=130,y=210)

#button insert
insert=Button(root,text="Insert")
insert.place(x=50,y=260)
#button view
view=Button(root,text="View")
view.place(x=100,y=260)

#button update
update=Button(root,text="Update")
update.place(x=160,y=260)

#button delete
delete=Button(root,text="Delete")
delete.place(x=220,y=260)




root.mainloop()