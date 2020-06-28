import tkinter as tk
from tkinter import *
import tkinter.font as TkFont
root = tk.Tk()
root.title('Form')
root.geometry("350x200")



font1 = TkFont.Font(family="Times",size=10,weight="bold")
font2 = TkFont.Font(family="Helvetica",size=12,weight="bold")
font3 = TkFont.Font(family="verdana",size=15,weight="bold")
font4 = TkFont.Font(family="opensans",size=20,weight="bold")
font5 = TkFont.Font(family="Symbol",size=25,weight="bold")
 

l1 = Label(root,text="This is first Font", font = font1,bg="red")
l1.pack()

l2  = Label(root,text="This is Second Font", font= font2,fg="red")
l2.pack()

l3  = Label(root,text="This is Third Font", font= font3)
l3.pack()

l4  = Label(root,text="This is Fourth Font", font= font4, fg="cyan")
l4.pack()

l5  = Label(root,text="This is Fifth Font", font= font5, fg="white",bg="black")
l5.pack()

l6  = Label(root,text="This is Last Font", font=("verdana",10,"bold"))
l6.pack()

root.mainloop()


