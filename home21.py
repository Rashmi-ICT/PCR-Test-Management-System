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




def ureg():
    os.system('python userreg.py')

def phreg():
    os.system('python phi_phi.py')

def asreg():
    os.system('python lab.py')

def login():
    os.system('python login.py')


def btnclick():
    messagebox.showinfo("Message","Button is clicked")


photo = PhotoImage(file="images/h1.png")
photo2 = PhotoImage(file="images/user.png")
photo3 = PhotoImage(file="images/phi2.png")
photo4 = PhotoImage(file="images/l.png")


#=======lebel====================

photo7 = PhotoImage(file="images/lo.png")
photo8 = PhotoImage(file="images/ur.png")
photo9 = PhotoImage(file="images/phi.png")
photo10 = PhotoImage(file="images/assi.png")


btn = Button(
    root,
    image=photo,
    command=login,
    border=2,

   




)
btn.place(x=855,y=500)


btn2 = Button(
    root,
    image=photo2,
    command=ureg,
    border=2,
)

btn2.place(x=855,y=530)


btn3 = Button(
    root,
    image=photo3,
    command=phreg,
    border=2,
)

btn3.place(x=855,y=560)

btn4 = Button(
    root,
    image=photo4,
    command=asreg,
    border=2,
)

btn4.place(x=855,y=590)




btn7 = Button(
    root,
    image=photo7,
    command=login,
    border=2,


)

btn7.place(x=570,y=500)
    



btn8 = Button(
    root,
    image=photo8,
    command=ureg,
    border=2,


)

btn8.place(x=570,y=530)
    


btn9 = Button(
    root,
    image=photo9,
    command=phreg,
    border=2,


)

btn9.place(x=570,y=560)
    

btn10 = Button(
    root,
    image=photo10,
    command=asreg,
    border=2,


)

btn10.place(x=570,y=590)
    



    





root.mainloop()









