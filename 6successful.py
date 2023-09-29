from tkinter import *
from tkinter.ttk import *
os6=Tk()
os6.title("REGISTRATION FORM")
os6.geometry("800x500")
os6.configure(background="RED")
os6.maxsize(800,600)
os6.minsize(800,600)

label1=Label(os6,text="Thank You",background='blue',foreground="white",font="Jokerman 35")
label2=Label(os6,text="Payment Successful!!!",background='blue',foreground="white",font="Jokerman 35")
e1 = Entry(os6)
e2 = Entry(os6)

label1.place(relx=0.35,rely=0.1)
label2.place(relx=0.2,rely=0.4)





os6.mainloop()