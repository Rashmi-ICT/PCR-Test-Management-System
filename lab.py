import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
frame = Tk()
frame.geometry("750x550")
frame.title("Registration Form")                        
frame["bg"] = "sky blue"
frame.resizable(False, False)


def dain():
    en1 = entry_0.get()
    en2 = entry_2.get()
    en3 = entry_3.get()
    en4 = entry_4.get()
    en5 = entry_5.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="covid"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO labs (name, labid, tel, email, branch) VALUES (%s, %s, %s, %s, %s)"
    val = (en1, en2, en3, en4, en5)
    #val = ('test', 'test', 'test', 'test', 'test')
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
        

canvas=Canvas(frame,width=1000,height=700)  
image=ImageTk.PhotoImage(Image.open("images/photo1.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
   
        


#Form Title

user_title = Label(frame,text ="LAB ASSISTANT ",width = 20,
                   font = ("courier new",30,"bold",)).place(x=70,y=50)
user_title = Label(frame,text ="REGISTRATION ",width = 20,
                   font = ("courier new",30,"bold",)).place(x=70,y=100)


#Create fields
lab_name = Label(frame,text = " NAME",width = 20,
                 font = ("arial",12,"bold"),anchor=W)
lab_name.place(x = 70,y = 180,)


entry_0=Entry(frame)
entry_0=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_0.place(x=300,y=180 ,width=250,height=25)




lab_id = Label(frame,text = "LAB ID",width = 20,
               font = ("arial",12,"bold"),anchor=W)
lab_id.place(x = 70,y = 230)

entry_2=Entry(frame)
entry_2=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_2.place(x = 300,y = 230,width=250,height=25)

lab_tp = Label(frame,text = "TP",width = 20,
               font = ("arial",12,"bold"),anchor=W)
lab_tp.place(x = 70,y = 280)



entry_3=Entry(frame)
entry_3=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_3.place(x = 300,y = 280,width=250,height=25)




lab_email = Label(frame,text = " EMAIL",width = 20,
                  font = ("arial",12,"bold"),anchor=W)
lab_email.place(x = 70,y = 330)



entry_4=Entry(frame)
entry_4=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_4.place(x = 300,y = 330,width=250,height=25)



lab_branch = Label(frame,text = "BRANCH",width = 20,
                   font = ("arial",12,"bold"),anchor=W)
lab_branch.place(x = 70,y = 380)

entry_5=Entry(frame)
entry_5=Entry(frame,font=("times new romen",12,"bold",),fg="black")
entry_5.place(x = 300,y = 380,width=250,height=25)

#cmd_branch=ttk.combobox(frame,text = " ANSWER",font=("arial",12,"bold")).place(x=100,y=400)
#cmd_branch['values']=("","","",)






Button(frame, text='Submit',width=10,bg='blue',command=dain,fg='white',font = ("courier new",10,)).place(x=150,y=460)
Button(frame, text='Clear Data',width=10,bg='blue',fg='white',command=clear,
                       font = ("courier new",10,)).place(x=380,y=460)


frame.mainloop()








