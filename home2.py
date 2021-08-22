import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import os




root = Tk()
root.geometry("1000x700")
root.title("Home Page")
root["bg"] = "#fff"
root.resizable(False, False)

canvas=Canvas(root,width=1000,height=700)  
image=ImageTk.PhotoImage(Image.open("images/Untitled-3.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()




def vre():
    os.system('python veiwreport.py')
    

def sumer():
    os.system('python summery.py')
   

def login():
    os.system('python login.py')



def btnclick():
    messagebox.showinfo("Message","Button is clicked")


photo = PhotoImage(file="images/h1.png")

photo5 = PhotoImage(file="images/s.png")

photo6 = PhotoImage(file="images/s1.png")


#=======lebel====================

photo7 = PhotoImage(file="images/lo.png")

photo11 = PhotoImage(file="images/vr.png")

photo12 = PhotoImage(file="images/rs.png")


btn = Button(
    root,
    image=photo,
    command=login,
    border=2,

   




)
btn.place(x=855,y=500)




btn5 = Button(
    root,
    image=photo5,
    command=vre,
    border=2,
)

btn5.place(x=855,y=538)





btn6 = Button(
    root,
    image=photo6,
    command=sumer,
    border=2,
)

btn6.place(x=855,y=575)





btn7 = Button(
    root,
    image=photo7,
    command=login,
    border=2,


)

btn7.place(x=570,y=500)
    


    

btn11 = Button(
    root,
    image=photo11,
    command=vre,
    border=2,


)

btn11.place(x=570,y=538)



btn12 = Button(
    root,
    image=photo12,
    command=sumer,
    border=2,


)

btn12.place(x=570,y=575)



    





root.mainloop()





