
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import tkinter as tk 
from tkinter import ttk
import mysql.connector

def dain():
    en1 = entry_0.get()
    en2 = entry_2.get()
    en3 = user_gender.get()
    en4 = entry_4.get()
    en5 = entry_5.get()
    en6 = entry_6.get()
    en7 = entry_7.get()
    en8 = entry_8.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="covid"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO phis (phi_name, phi_id, gender, address, email, tel, phi_division, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (en1, en2, en3, en4, en5, en6, en7, en8)
    #val = ('test', 'test', 'test', 'test', 'test', 'test', 'test', '202.03.21')
    mycursor.execute(sql, val)

    mydb.commit()
    
def clear():
        #clear output area
        #   output.delete(0.0,END)
        
        entry_0.delete(0,END)
        #entry_1.delete(0,END)
        entry_2.delete(0,END)
        entry_3.delete(0,END)
        entry_4.delete(0,END)
        entry_5.delete(0,END)
        entry_6.delete(0,END)
        entry_7.delete(0,END)
        entry_8.delete(0,END)
        #entry_9.delete(0,END)
        #entry_10.delete(0,END)


frame = tk.Tk()
frame.geometry("650x650")
frame.title("Registration Form")                        
frame["bg"] = "#77D0E8"
frame.resizable(False, False)

canvas=Canvas(frame,width=1000,height=700)  
image=ImageTk.PhotoImage(Image.open("images/photo1.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#===variable===

user_gender = StringVar()
        


#Form Title

user_title = Label(frame,text ="PHI Registration ",width = 20,
                   font = ("courier new",30,"bold",)).place(x=70,y=50)


#Create fields
phi_name = Label(frame,text = "PHI NAME",width = 20,
                   font = ("arial",10,),anchor=W)
phi_name.place(x = 70,y = 130)


entry_0=Entry(frame)
entry_0=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_0.place(x=300,y=130 ,width=250,height=25)




user_id = Label(frame,text = "PHI ID",width = 20,
                   font = ("arial",10,),anchor=W)
user_id.place(x = 70,y = 180)

entry_2=Entry(frame)
entry_2=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_2.place(x = 300,y = 180,width=250,height=25)

u_gender =Label(frame,text="GENDER",width=20,
                font=("times new romen",10,),anchor=W)
u_gender.place(x=70,y=230 )

#user_3=Entry(frame)
#entry_3=Entry(frame,font=("times new romen",10,"bold",),fg="black")
#user_3.place(x=300,y=230 ,width=250,height=25)


g_radio_male=Radiobutton(frame,text="Male",padx= 5, variable=user_gender ,value= 1,width=8,
            font=("times new romen",0,"bold")).place(x=300,y=230)
g_radio_female=Radiobutton(frame,text="Female",padx= 12, variable=user_gender, value= 2,width=10,
            font=("times new romen",0,"bold")). place(x=398,y=230)


user_address = Label(frame,text = "USER ADDRESS",width = 20,
                     font = ("arial",10,),anchor=W)
user_address.place(x = 70,y = 280)

entry_4=Entry(frame)
entry_4=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_4.place(x = 300,y = 280,width=250,height=25)


user_email = Label(frame,text = "PHI EMAIL",width = 20,
                     font = ("arial",10,),anchor=W)
user_email.place(x = 70,y = 330)



entry_5=Entry(frame)
entry_5=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_5.place(x = 300,y = 330,width=250,height=25)




user_tp = Label(frame,text = "PHI TP",width = 20,
                     font = ("arial",10,),anchor=W)
user_tp.place(x = 70,y = 380)

entry_6=Entry(frame)
entry_6=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_6.place(x = 300,y = 380,width=250,height=25)



phi_divition = Label(frame,text = "PHI DIVITION",width = 20,
                       font = ("arial",10,),anchor=W)
phi_divition.place(x = 70,y = 430)

entry_7=Entry(frame)
entry_7=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_7.place(x = 300,y = 430,width=250,height=25)



user_date= Label(frame,text = "DATE",width = 20,
                       font = ("arial",10,),anchor=W)
user_date.place(x = 70,y = 480)

entry_8=Entry(frame)
entry_8=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_8.place(x = 300,y = 480,width=250,height=25)



Button(frame, text='Submit',width=10,bg='blue',command=dain,fg='white',
                       font = ("courier new",10,)).place(x=100,y=550)
Button(frame, text='Clear Data',width=10,bg='blue',fg='white',command=clear,
                       font = ("courier new",10,)).place(x=320,y=550)







frame.mainloop()


