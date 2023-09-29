import mysql.connector as sq
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from subprocess import call

os2=Tk()
os2.title("REGISTRATION FORM-The Banyan Tree School")
os2.geometry('800x500')
os2.maxsize(800,600)
os2.minsize(800,600)
os2.configure(background="grey")

a1=StringVar()
b1=StringVar()
head1=Label(os2,text="   LOGIN FORM", background="RED", font="algerian 35", foreground="BLUE",width=12)
head1.place(relx=0.30)
a = Label(os2,text="User_id", width=30, background="grey",font="bold").place(relx=0.37,rely=0.38)
Entry(os2,textvariable=a1).place(relx=0.47,rely=0.38,width=150)
b = Label(os2,text="Password", width=30, background="grey",font="bold").place(relx=0.37,rely=0.45)
Entry(os2,textvariable=b1).place(relx=0.47,rely=0.45,width=150)

def login():
    mycon = sq.connect(host="localhost",database="project",user="root",passwd="root")
    cur = mycon.cursor()
    if (a1.get()=='ritik' and b1.get()=='12345'):
        call(["python", "registration.py"])
    else:
        tkinter.messagebox.showinfo("Try again","user id or password is incorrect")

d = Button(os2, text="SUBMIT", command=login)
d.place(relx=0.41,rely=0.70,height=35,width=200)
os2.mainloop()