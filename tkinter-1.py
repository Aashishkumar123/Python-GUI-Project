#importing 
from tkinter import *
import tkinter as tk

#calling Tk() method
root = tk.Tk() 
#its used for creating gui window 

#title() method is used to change the title 
root.title("My GUI")

#geometry() method is used to resize the Gui Window
root.geometry("250x250")

#maxsize() method is used for define the maximum size of the window
root.maxsize(300,300)

#minsize() method is used for define the minimum size of the window
root.minsize(200,200)

#mainloop() is used to load the GUI Window
root.mainloop()
