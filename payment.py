from tkinter import *
import mysql.connector as sqltor
from tkinter.ttk import *
from subprocess import call

os7=Tk()
os7.title("REGISTRATION FORM-The Banyan Tree School")

os7.geometry("800x500")
os7.configure(background="grey")
os7.maxsize(800,600)
os7.minsize(800,600)

cash_amt=StringVar()
Serial_no=StringVar()
head1=Label(os7,text="      PAYMENT", background="RED", font="algerian 35", foreground="BLUE",width=12)
head1.place(relx=0.30)
label1=Label(os7,text="Enter Serial No",background="grey",foreground="black").place(relx=0.37,rely=0.3)
label2=Label(os7,text="Enter Amount",background="grey",foreground="black").place(relx=0.37,rely=0.4)
l1=Entry(os7,textvariable=cash_amt).place(relx=0.5,rely=0.3)
l2=Entry(os7,textvariable=Serial_no).place(relx=0.5,rely=0.4)
def sub():
    mycon = sqltor.connect(host="localhost", database="project", user="root", passwd="root")
    cur = mycon.cursor()
    cur.execute("insert into cash values('"+Serial_no.get()+"','"+cash_amt.get()+"')")
    mycon.commit()
    call(["python","successful.py"])

bu1=Button(os7,text="SUBMIT",command=sub,width="20")

bu1.place(relx=0.45,rely=0.6)

os7.mainloop()

