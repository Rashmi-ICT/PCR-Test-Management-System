from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk,Image
import mysql.connector
import os


def loginselect():
    print('call')
    en1 = v.get()
    en2 = entry_1.get()
    en3 = entry_2.get()


    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="covid"
    )

    mycursor = mydb.cursor()

    if '1' in en1:

        mycursor.execute("SELECT phi_id,email FROM phis")

        myresult = mycursor.fetchall()

        for x in myresult:
            if en2 in x:
                if en3 in x:
                    os.system('python home2.py')

    elif '2' in en1:

        mycursor.execute("SELECT nic,email FROM users")

        myresult = mycursor.fetchall()

        for x in myresult:
            if en2 in x:
                if en3 in x:
                    os.system('python home22.py')

    elif '3' in en1:

        mycursor.execute("SELECT labid,email FROM labs")

        myresult = mycursor.fetchall()

        for x in myresult:
            if en2 in x:
                if en3 in x:
                    os.system('python homelab1.py')




login = Tk()
login.geometry("1000x615")
login.title("LOGIN FORM")                        
login["bg"] = "#fff"


canvas=Canvas(login,width=1100,height=1000)  
image=ImageTk.PhotoImage(Image.open("images/bg02.jpg"))

canvas.create_image(30,0,anchor=NW,image=image)
canvas.pack()

#===variable===

v = StringVar()





#form feild

login_title = Label(login,text ="PCR TEST MANEGMENT ",width = 26,font = ("Impact",30,"bold"),fg="#03506f").place(x=130,y=50)
login_title = Label(login,text ="SYSTEM ",width = 26,font = ("Impact",30,"bold"),fg="#03506f").place(x=130,y=100)

    
userSelect_Frame = Frame(login, bg='#d0e8f2')
userSelect_Frame.place(x=130, y=150, height=350, width=550)




     #==============================radio button====================================

Radiobutton(login, text="PHI", padx=11, variable=v, value=1, width=10, font=("Impact", 15, ),fg="#03506f").place(x=150,
                                                                                                                 y=200)

Radiobutton(login, text="PATIENT", padx=12, variable=v, value=2, width=12, font=("Impact", 15, ),fg="#03506f").place(
    x=290, y=200)

Radiobutton(login, text="LAB ASSISTANT", padx=20, variable=v, value=3, width=15,
            font=("Impact", 15, ),fg="#03506f").place(x=440, y=200)

#=================================user box=======================================

user_image = PhotoImage(file="images/userName.png")
userName_Label = Label(
login, image=user_image, bg='#d0e8f2', width=50, height=50)
userName_Label.place(x=140,y=250)
    
login_1 =Label(login,text="USER NAME", width=20,font=("times new romen",12,"bold"),fg="gray")
login_1.place(x=200,y=260,height=30)


entry_1=Entry(login,font=("times new romen",12,"bold"),fg="#2B5A79")
entry_1.place(x=400,y=260 ,width=250,height=30)

   #===================================password box================================
pwd_image = PhotoImage(file="images/pw.png")
pwd_pic_Label = Label(login, image=pwd_image,
                              bg='#d0e8f2', width=50, height=50)
pwd_pic_Label.place(x=140,y=350)




login_2 =Label(login,text="PASSWORD", width=20,font=("times new romen",12,"bold"),fg="gray")
login_2.place(x=200,y=360,height=30)


entry_2=Entry(login,font=("times new romen",12,"bold"),fg="#2B5A79",show="*")
entry_2.place(x=400,y=360 ,width=250,height=30)



def iExit():
    userRespond = tkinter.messagebox.askokcancel(
                "PCR SYSTEM", "Confirm if you want to exit")

    if userRespond > 0:
        login.destroy()
        return


def regselect():
    os.system('python home21.py')

           






    #===================================radio button=================================

Button(login, text='LOGIN',width=14, command=loginselect,height=1,bg='blue',fg='white',font=("times new romen",10,"bold")).place(x=200,y=450)

Button(login, text='REGISTRATION',width=14, command=regselect,height=1,bg='blue',fg='white',font=("times new romen",10,"bold")).place(x=370,y=450)




Button(login, text='EXIT',width=14,command=iExit,height=1,bg='blue',fg='white',font=("times new romen",10,"bold")).place(x=530,y=450)



login.mainloop()

