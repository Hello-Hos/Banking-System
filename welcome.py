from tkinter import *
import mysql.connector as  sq
from tkinter.ttk import *
from tkinter import font
from subprocess import call
os1=Tk()
os1.title("REGISTRATION FORM-The Banyan Tree School")
os1.configure(background="red")
os1.geometry('800x500')
os1.maxsize(800,600)
os1.minsize(800,600)

a2=Label(os1,text="Welcome!!!",background='blue',foreground="white",font="Jokerman 50")
a2.place(relx=0.25)

def login():
    call(["python","login.py"])

a3=Button(os1,text="SIGN IN",command=login).place(relx=0.37,rely=0.3,height=50,width=200)

def login():
    call(["python","loginupdate.py"])
a4=Button(os1,text="UPDATE",command=login)
a4.place(relx=0.37,rely=0.6,height=50,width=200)

os1.mainloop()
