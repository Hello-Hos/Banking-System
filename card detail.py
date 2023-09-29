from tkinter import *
from tkinter.ttk import *
import mysql.connector as sqltor
from subprocess import call

os5=Tk()
os5.title("REGISTRATION FORM-The Banyan Tree School")
os5.geometry('800x500')
os5.maxsize(800,600)
os5.minsize(800,600)
os5.configure(background="grey")
#a0=StringVar()
card_no=StringVar()
month=StringVar()
year=StringVar()
cvv=StringVar()
Amount=StringVar()
label0=Label(os5,text="Enter card detail",foreground="blue",font="Algerian 35",background='red')
label1=Label(os5,text="Card Number",background="grey",font="bold")
label2=Label(os5,text="MM",background="grey",font="bold")
label3=Label(os5,text="YY",background="grey",font="bold")
label4=Label(os5,text="CVV",background="grey",font="bold")

def pay():
    mycon = sqltor.connect(host="localhost", user="root", passwd="root", database="project")
    cursor = mycon.cursor()
    cursor.execute("insert into card_details values('" +card_no.get()+ "','" +month.get()+ "','" +year.get()+ "','" +cvv.get()+ "')")
    mycon.commit()

    call(["python","payment.py"])
bu1 = Button(os5,text ="Next", width=15,command=pay)
e1 = Entry(os5,textvariable=card_no)
e2 = Entry(os5,textvariable=month)
e3 = Entry(os5,textvariable=year)
e4 = Entry(os5,textvariable=cvv)

label0.place(relx=0.2,rely=0)
label1.place(relx=0.2,rely=0.3)
label2.place(relx=0.2,rely=0.4)
label3.place(relx=0.2,rely=0.5)
label4.place(relx=0.2,rely=0.6)
bu1.place(relx=0.4,rely=0.9)

e1.place(relx=0.6,rely=0.3)
e2.place(relx=0.6,rely=0.4)
e3.place(relx=0.6,rely=0.5)
e4.place(relx=0.6,rely=0.6)

os5.mainloop()