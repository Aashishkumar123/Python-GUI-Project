import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('Form')
root.geometry("250x160")

#variable
var = IntVar()
#label
l1 = Label(root,text="Radio Buttons",font=("verdana",10,"bold"))
l1.grid(sticky="w",padx=60)

#radiobuttons
r1 = Radiobutton(root,text="R1", value=1,variable=var)
r1.grid(sticky="w",row=1,pady=10)

r2 = Radiobutton(root,text="R2", value=2,variable=var,relief=RIDGE)
r2.grid(sticky="w",row=1,padx=60,pady=10)

r3 = Radiobutton(root,text="R3", value=3,variable=var,relief=SUNKEN)
r3.grid(sticky="w",row=1,padx=120,pady=10)

r4 = Radiobutton(root,text="R4", value=4,variable=var,relief=RIDGE,bg="red",fg="white")
r4.grid(sticky="w",row=1,padx=180,pady=10)

#label
l2 = Label(root,text="Check Buttons",font=("verdana",10,"bold"))
l2.grid(sticky="w",padx=60)

#checkbuttons
c1 = Checkbutton(root,text="C1")
c1.grid(row=3,sticky="w",pady=10)

c2 = Checkbutton(root,text="C2",relief=SUNKEN)
c2.grid(row=3,sticky="w", padx=60,pady=10)

c3 = Checkbutton(root,text="C3",relief=RIDGE)
c3.grid(row=3,sticky="w", padx=120,pady=10)

c4 = Checkbutton(root,text="C4",relief=SUNKEN,bg="cyan",fg="white")
c4.grid(row=3,sticky="w", padx=180,pady=10)

root.mainloop()


