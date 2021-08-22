from tkinter import *
from PIL import ImageTk,Image
import mysql.connector


def dataselect():
    en = entry_0.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="covid"
    )

    mycursor = mydb.cursor()

    sql = "select * from users where nic = %s"

    mycursor.execute(sql,(en,))

    myresult = mycursor.fetchall()

    for x in myresult:
        print("Name = ", x[1], )
        print("Age = ", x[2])
        print("Nic = ", x[3])
        print("Gender  = ", x[4] )
        print("Address  = ", x[5])
        print("Email  = ", x[6])
        print("Division  = ", x[7])
        print("Tel  = ", x[8])
         
        

    cursor = mydb.cursor()

    my_sql = "select * from pns where user_id = %s"

    cursor.execute(my_sql, (en,))

    result = cursor.fetchall()

    for row in result:
        le = row[2]

        if '1' in le:
            print('Level  =  Positive')
            print("GET TO THE HOSPITAL RIGHT AWAY")
        else:
            print('Level  =  Negative')
            print("FOLLOW HEALTH CARE GUIDLINES")


frame = Tk()
frame.geometry("650x350")
frame.title("REPORT")
frame["bg"] = "sky blue"

canvas=Canvas(frame,width=700,height=400)  
image=ImageTk.PhotoImage(Image.open("images/photo1.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#

user_title = Label(frame, text="VIWE REPORT ", width=20, font=("courier new", 30, "bold",)).place(x=70, y=50)

# Create fields
phi_name = Label(frame, text="PATIENT ID", width=20, font=("arial", 10,))
phi_name.place(x=70, y=130)

entry_0 = Entry(frame)
entry_0.place(x=300, y=130, width=250, height=25)
"""
user_id = Label(frame, text="PATIENT NAME", width=20, font=("arial", 10,))
user_id.place(x=70, y=180)

entry_2 = Entry(frame)
entry_2.place(x=300, y=180, width=250, height=25)
"""
Button(frame, text='Submit',command=dataselect, width=10, bg='blue', fg='white', font=("courier new", 10,)).place(x=130, y=250)
Button(frame, text='Clear Data', width=10, bg='blue', fg='white', font=("courier new", 10,)).place(x=300, y=250)

frame.mainloop()
