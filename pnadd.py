import mysql.connector
from tkinter import *
from PIL import ImageTk,Image


def datain():

    en1 = entry_0.get()
    en2 = level.get()
    en3 = entry_8.get()
    en4 = entry_2.get()
    en4 = en4.lower()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="covid"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO pns (user_id, Level,division, date) VALUES (%s, %s, %s, %s)"
    val = (en1, en2,en4, en3)
    mycursor.execute(sql, val)

    mydb.commit()


frame = Tk()
frame.geometry("600x450")
frame.title("P & N FORM")
frame["bg"] = "sky blue"


canvas = Canvas(frame, width=1100, height=1000)
image = ImageTk.PhotoImage(Image.open("images/photo1.png"))
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

level = StringVar()

#Form Title
user_1=Label(frame,bg="sky blue")
#user_1.place(x=400,y=100,width=700,height=500)

user_title = Label(frame,text ="P & N DETAILS ",width = 20,font = ("courier new",30,"bold",)).place(x=70,y=50)

# Create fields
phi_name = Label(frame, text="PATIENT ID", width=20, font=("arial", 10,),anchor = W)
phi_name.place(x=70, y=140)

entry_0 = Entry(frame)
entry_0.place(x=300, y=140, width=250, height=25)

user_id = Label(frame, text="DIVITION", width=20, font=("arial", 10,),anchor = W)
user_id.place(x=70, y=180)

entry_2 = Entry(frame)
entry_2.place(x=300, y=180, width=250, height=25)

user_gender = Label(frame, text="LEVEL", width=20, font=("arial", 10,),anchor = W)
user_gender.place(x=70, y=220)

# entry_3=Entry(frame)
# entry_3.place(x = 240,y = 250)


g_radio_male = Radiobutton(frame, text="NEGATIVE", padx=25, variable=level, value=0).place(x=300, y=220)
g_radio_female = Radiobutton(frame, text="POSITIVE", padx=30, variable=level, value=1).place(x=405, y=220)


user_date = Label(frame, text="DATE", width=20, font=("arial", 10,),anchor = W)
user_date.place(x=70, y=260)

entry_8 = Entry(frame)
entry_8.place(x=300, y=260, width=250, height=25)

# entry_date.place(x = 240,y = 520)


Button(frame, text='Submit', command=datain, width=10, bg='blue', fg='white', font=("courier new", 10,)).place(x=100, y=320)
Button(frame, text='Clear Data', width=10, bg='blue', fg='white', font=("courier new", 10,)).place(x=320, y=320)

frame.mainloop()
