from tkinter import *
from tkinter.ttk import *
from subprocess import call
os4=Tk()
os4.title("REGISTRATION FORM")
os4.geometry("800x500")
os4.maxsize(800,600)
os4.minsize(800,600)
os4.config(background="grey")
label1=Label(os4,text="Select payment mode",background="RED",width="19",font="algerian 35",foreground="blue")
label2=Label(os4,text="Payment Modes available",background="grey",font="jokerman 25",foreground="yellow")
def deb_crd():
    call(["python","5card detail.py"])
bu1 = Button(os4,text ="Debit/Credit",width=15,command=deb_crd)
bu3 = Button(os4,text ="Net Banking",width=15)

def cash():
    call(["python","cash payment.py"])
bu4 = Button(os4,text ="Cash",width=15,command=cash)


label1.place(relx=0.20)
label2.place(relx=0.27,rely=0.33)
bu1.place(relx=0.45,rely=0.45,width=100,height=50)
#bu2.grid(row=4,column=0,pady =4)
bu3.place(relx=0.45,rely=0.55,width=100,height=50)
bu4.place(relx=0.45,rely=0.65,width=100,height=50)


os4.mainloop()