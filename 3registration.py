import mysql.connector as sqltor
from tkinter import *
from tkinter.ttk import *
from subprocess import call

os=Tk()
os.title("REGISTRATION FORM")
os.geometry("800x500")
os.configure(background="grey")
os.maxsize(800,600)
os.minsize(800,600)
f_name = StringVar()
fs_name=StringVar()    
ms_name=StringVar()
sr_no=StringVar()
con_no=StringVar()
add=StringVar()
pin=StringVar()
 
def hk():

    mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="project")
    cursor=mycon.cursor()
    cursor.execute("insert into project2 values('"+f_name.get()+"','"+fs_name.get()+"','"+ms_name.get()+"','"+sr_no.get()+"','"+con_no.get()+"','"+add.get()+"','"+pin.get()+"')")

    mycon.commit()
    call(["python", "4payment mode.py"])



label1=Label(os,text="  Admission form",background="RED",width="15",font="algerian 35",foreground="BLUE")
label2=Label(os,text="Full Name",background="grey",foreground='black',font="bold")
label3=Label(os,text="Father's Name",background='grey',foreground='black',font="bold")
label4=Label(os,text="Mother's Name",background='grey',foreground='black',font="bold")
label5=Label(os,text="Serial No.",background='grey',foreground='black',font="bold")
label6=Label(os,text="contact no",background="grey",foreground='black',font="bold")
label7=Label(os,text="Address",background="grey",foreground='black',font="bold")
label8=Label(os,text="Pin code",background="grey",foreground='black',font="bold")
bu1 =Checkbutton(os,text="Save data")



bu2 =Button(os,text="submit data",command=hk,width="20")
gen1=Radiobutton(os,text='female',value=1,width="6")
gen2=Radiobutton(os,text='male',value=2,width="6")


user2=Entry(os,width="35",textvariable=f_name)
user3=Entry(os,width="35",textvariable=fs_name)
user4=Entry(os,width="35",textvariable=ms_name)
user5=Entry(os,width="35",textvariable=sr_no)
user6=Entry(os,width="35",textvariable=con_no)
user7=Entry(os,width="35",textvariable=add)
user8=Entry(os,width="35",textvariable=pin)


label1.grid(row=0,column=1,pady=0,padx=25)
label2.grid(row=1,column=0,pady=15,padx=25)
label3.grid(row=2,column=0,pady=15,padx=50)
label4.grid(row=3,column=0,pady=15,padx=50)
label5.grid(row=4,column=0,pady=15,padx=50)
label6.grid(row=5,column=0,pady=15,padx=50)
label7.grid(row=6,column=0,pady=15,padx=50)
label8.grid(row=7,column=0,pady=15,padx=50)
bu1.place(relx=0.20,rely=0.82)
bu2.place(relx=0.47,rely=0.82)
gen1.grid(row=9,column=1,pady=10)
gen2.grid(row=10,column=1)

user2.grid(row=1,column=1)
user3.grid(row=2,column=1)
user4.grid(row=3,column=1)
user5.grid(row=4,column=1)
user6.grid(row=5,column=1)
user7.grid(row=6,column=1)
user8.grid(row=7,column=1)

os.mainloop()
