# import tkinter module 
from tkinter import * 
import tkinter as tk

# creating main tkinter window/toplevel 
root = tk.Tk() 

root.geometry("230x120")
root.title('Form')

# Lable() function creates a label widget 

l1 = Label(root, text = "Email:") 
l2 = Label(root, text = "Password:") 

# grid method to arrange labels in respective 
# rows and columns as specified 

l1.grid(row = 1, column = 1, pady = 10,padx=15) 
l2.grid(row = 2, column = 1, pady = 4,padx=15) 

# entry widgets, used to take entry from user 
e1 = Entry(root) 
e2 = Entry(root) 

# this will arrange entry widgets 
e1.grid(row = 1, column = 2, pady = 10) 
e2.grid(row = 2, column = 2, pady = 4) 

# Button() function is used to create button widgets
submit = Button(root,text="submit")
submit.grid(column=2,row=3,pady="3")
mainloop() 
