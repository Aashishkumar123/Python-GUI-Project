# Image resources are provided in the file
# Make sure you change the paths in the code

from tkinter import *
from PIL import ImageTk , Image

rt = Tk()
rt.title("Basic Calculator")
#Change path of ico file here
rt.iconbitmap('C:/imgs/icons/calc512px.ico') #CHANGE PATH INSIDE ''
rt.geometry("300x430")
#change path of Background file here
bg = ImageTk.PhotoImage(file="C:/imgs/300x430_bg.png") #CHANGE PATH INSIDE " "
bg_label = Label(rt, image=bg).place(x=0,y=0)

# Entry Widget

e = Entry(rt,width=35,borderwidth=10,font=("Times",10))
e.grid(row=0,column=0,pady=20,padx=30,columnspan=3)

# CHANGE YOUR PATHS HERE..!!!!!
# Example Img1 = ImageTk.PhotoImage(file="YOUR PATH HERE")

Img1 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/1.png")
Img2 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/2.png")
Img3 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/3.png")
Img4 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/4.png")
Img5 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/5.png")
Img6 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/6.png")
Img7 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/7.png")
Img8 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/8.png")
Img9 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/9.png")
Img0 = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/10.png")
ImgA = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/11.png")
ImgS = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/12.png")
ImgM = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/13.png")
ImgD = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/14.png")
ImgE = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/15.png")
ImgCLR = ImageTk.PhotoImage(file="C:/Users/irfan/OneDrive/Desktop/MO TECH/pngs50x50/16.png")



def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    

def button_add():
    first_number = e.get()
    global f_num
    global maths
    maths = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    

def button_sub():
    first_number = e.get()
    global f_num
    global maths
    maths = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global maths
    maths = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_mult():
    first_number = e.get()
    global f_num
    global maths
    maths = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_equals():
    second_number = e.get()
    e.delete(0, END)
    
    if maths == "addition":
        e.insert(0, f_num+int(second_number))
    if maths == "subtraction":
        e.insert(0, f_num-int(second_number))
    if maths == "multiplication":
        e.insert(0, f_num*int(second_number))
    if maths == "division":
        e.insert(0, f_num/int(second_number))


def button_clear():
    e.delete(0,END)

 # Defining Buttons
button1 = Button(rt,border="3",image=Img1,command= lambda:button_click(1)).grid(row= 1,column=0)
button2 = Button(rt,border="3",image=Img2,command= lambda:button_click(2)).grid(row= 1,column=1)
button3 = Button(rt,border="3",image=Img3,command= lambda:button_click(3)).grid(row= 1,column=2)
button4 = Button(rt,border="3",image=Img4,command= lambda:button_click(4)).grid(row= 2,column=0)
button5 = Button(rt,border="3",image=Img5,command= lambda:button_click(5)).grid(row= 2,column=1)
button6 = Button(rt,border="3",image=Img6,command= lambda:button_click(6)).grid(row= 2,column=2)
button7 = Button(rt,border="3",image=Img7,command= lambda:button_click(7)).grid(row= 3,column=0)
button8 = Button(rt,border="3",image=Img8,command= lambda:button_click(8)).grid(row= 3,column=1)
button9 = Button(rt,border="3",image=Img9,command= lambda:button_click(9)).grid(row= 3,column=2)
button0 = Button(rt,border="3",image=Img0,command= lambda:button_click(0)).grid(row= 4,column=1)
buttonA = Button(rt,border="3",image=ImgA,command= button_add).grid(row= 4,column=2)
buttonS = Button(rt,border="3",image=ImgS,command= button_sub).grid(row= 4,column=0)
buttonM = Button(rt,border="3",image=ImgM,command= button_mult).grid(row= 5,column=1)
buttonD = Button(rt,border="3",image=ImgD,command= button_div).grid(row= 5,column=0)
buttonE = Button(rt,border="3",image=ImgE,command= button_equals).grid(row= 5,column=2)
buttonCLR=Button(rt,border="3",image=ImgCLR,command=button_clear).grid(row= 6,column=1)

rt.mainloop()
