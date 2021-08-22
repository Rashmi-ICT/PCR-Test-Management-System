import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

summery = Tk()
summery.geometry("750x450")
summery.title("summery Form")                        
summery["bg"] = "sky blue"
summery.resizable(False, False)

canvas=Canvas(summery,width=750,height=450)  
image=ImageTk.PhotoImage(Image.open("images/photo1.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()




def vire():
    p = 0
    n = 0
    en1 = entry_0.get()
    en1 = en1.lower()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="covid"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM pns")

    myresult = mycursor.fetchall()

    for x in myresult:
        if en1 in x:
            if '0' in x:
                n = n+1
            elif '1' in x:
                p = p+1


    lab_id = Label(summery, text="NUMBER OF NEGITIVE PATIENTS  :", width=30, font=("arial", 12, "bold"))
    lab_id.place(x=70, y=230)

    entry_2 = Label(summery, text=n, width=30, font=("arial", 12, "bold"))
    entry_2.place(x=400, y=230, width=250, height=25)

    lab_tp = Label(summery, text="NUMBER OF POSITIVE PATIENTS  :", width=30, font=("arial", 12, "bold"))
    lab_tp.place(x=70, y=280)

    entry_5 = Label(summery, text=p, width=30, font=("arial", 12, "bold"))
    entry_5.place(x=400, y=280, width=250, height=25)


#Form Title
user_1=Label(summery,bg="sky blue")
user_1.place(x=400,y=100)

summery_title = Label(summery,text ="SUMMERY ",width = 20,font = ("courier new",30,"bold",)).place(x=70,y=50)

#cmd_branch=ttk.combobox(summery,text = " ANSWER",font=("arial",12,"bold")).place(x=100,y=400)
#cmd_branch['values']=("","","",)

#Create fields
lab_name = Label(summery,text = " SELECT DISTRICT  :",width = 30,font = ("arial",12,"bold"))
lab_name.place(x = 70,y = 180)


entry_0=Entry(summery)
entry_0.place(x=400,y=180 ,width=250,height=25)

Button(summery, text='GET DATA',command=vire,width=10,bg='blue',fg='white',font = ("courier new",10,)).place(x=330,y=340)



summery.mainloop()








