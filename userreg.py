import mysql.connector
from tkinter import *
from PIL import ImageTk,Image


def dain():
    en1 = entry_1.get()
    en2 = entry_2.get()
    en3 = entry_3.get()
    en4 = entry_4.get()
    en5 = entry_5.get()
    en6 = entry_6.get()
    en7 = entry_9.get()
    en8 = entry_8.get()
    en9 = entry_10.get()


    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="covid"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO users (name, age, nic, gender, address, email, division, tel, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (en1, en2, en4, en3, en5, en6, en7, en8, en9)
    #val = ('test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', '202.03.21')
    mycursor.execute(sql, val)

    mydb.commit()


def clear():
        #clear output area
        #   output.delete(0.0,END)

        entry_1.delete(0,END)
        entry_2.delete(0,END)
        entry_3.delete(0,END)
        entry_4.delete(0,END)
        entry_5.delete(0,END)
        entry_6.delete(0,END)
       # entry_7.delete(0,END)
        entry_8.delete(0,END)
        entry_9.delete(0,END)
        entry_10.delete(0,END)
       

 
user = Tk()

user.geometry("600x700")
user.resizable(False, False)
user.config(bg="#10EBD7")

canvas=Canvas(user,width=1000,height=800)  
image=ImageTk.PhotoImage(Image.open("images/photo1.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()






user.title('REGISTRATION FORM')


user_0 = Label(user,bg="#fff",text="REGISTRATION FORM ", width=20,
               font=("times new romen",20,"bold"),fg="black")

user_0.place(x=120,y=40)


user_1 =Label(user,text="FULL NAME", width=20,
               font=("times new romen",12,),fg="gray",anchor=W)
user_1.place(x=50,y=130)


entry_1=Entry(user)
entry_1=Entry(user,font=("times new romen",12,"bold",),fg="black")
entry_1.place(x=300,y=130 ,width=250,height=25)


user_2 =Label(user,text="USER AGE", width=20,
               font=("times new romen",12,),fg="gray",anchor=W)
user_2.place(x=50,y=180)

entry_2=Entry(user)
entry_2=Entry(user,font=("times new romen",12,"bold",),fg="black")
entry_2.place(x=300,y=180,width=250,height=25)

#==Gender==

user_3 =Label(user,text="GENDER",width=20,
                font=("times new romen",12,),fg="gray",anchor=W)
user_3.place(x=50,y=230 )

user_3=Entry(user)
entry_3=Entry(user,font=("times new romen",12,"bold",),fg="black")
user_3.place(x=300,y=230 ,width=250,height=25)




var=IntVar()

#==Radio button==
Radiobutton(user,text="Male",padx= 5, variable= var, value=1,width=8,
            font=("times new romen",0,"bold")).place(x=300,y=230)
Radiobutton(user,text="Female",padx= 12, variable= var, value=2,width=10,
            font=("times new romen",0,"bold")).place(x=398,y=230)


label_4=Label (user,text="USER NIC",width=20,
            font=("times new romen",12,),fg="gray",anchor=W)
label_4.place(x=50,y=280)

entry_4=Entry(user)
entry_4=Entry(user,font=("times new romen",12,"bold",),fg="black")
entry_4.place(x=300,y=280 ,width=250,height=25)



label_5=Label(user,text="USER ADRESS",width=20,
              font=("times new romen",12,),fg="gray",anchor=W)
label_5.place(x=50,y=330)

entry_5=Entry(user)
entry_5=Entry(user,font=("times new romen",12,"bold",),fg="black")
entry_5.place(x=300,y=330 ,width=250,height=25)

label_6=Label(user,text="USER E-MAIL",width=20,
              font=("times new romen",12,),fg="gray",anchor=W)
label_6.place(x=50,y=380)

entry_6=Entry(user)
entry_6=Entry(user,font=("times new romen",12,"bold",),fg="black")
entry_6.place(x=300,y=380 ,width=250,height=25)

label_8=Label(user,text="USER TP",width=20,
              font=("times new romen",12,),fg="gray",anchor=W)
label_8.place(x=50,y=430)

entry_8=Entry(user)
entry_8=Entry(user,font=("times new romen",12,"bold",),fg="black")
entry_8.place(x=300,y=430 ,width=250,height=25)

# place district===
label_9=Label(user,text="USER DISTRICT",width=20,
              font=("times new romen",12,),fg="gray",anchor=W)
label_9.place(x=50,y=480)

#==== dropdownlist.
entry_9=Entry(user)
entry_9=Entry(user,font=("times new romen",12,"bold",),fg="black")
entry_9.place(x=300,y=480 ,width=250,height=25)



label_10=Label(user,text="DATE",width=20,
              font=("times new romen",12,),fg="gray",anchor=W)
label_10.place(x=50,y=530)

entry_10=Entry(user)
entry_10=Entry(user,font=("times new romen",12,"bold",),fg="black")
entry_10.place(x=300,y=530 ,width=250,height=25)







Button(user, text='Submit',width=14,bg='blue', command=dain,fg='white',
             font=("times new romen",10,"bold")).place(x=100,y=600)
Button(user, text='Clear Data',width=14,bg='blue',command=clear,fg='white',
             font=("times new romen",10,"bold")).place(x=300,y=600)


user.mainloop()








