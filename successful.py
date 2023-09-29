from tkinter import *
from tkinter.ttk import *
os6=Tk()
os6.title("REGISTRATION FORM-The Banyan Tree School")
os6.geometry("800x500")
os6.configure(background="RED")
os6.maxsize(800,600)
os6.minsize(800,600)

label1=Label(os6,text="Thank You",background='blue',foreground="white",font="Algerian 30")
label2=Label(os6,text="Payment Successful!!!",background='blue',foreground="white",font="Algerian 30")
label3=Label(os6,text="You are successfully Registered",background='blue',foreground="white",font="Algerian 15")

label1.place(relx=0.35,rely=0.1)
label2.place(relx=0.2,rely=0.4)
label3.place(relx=0.27,rely=0.7)

os6.mainloop()