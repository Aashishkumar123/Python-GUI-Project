from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("my GUI")
root.geometry("250x150")
img = ImageTk.PhotoImage(Image.open(r'C:\Users\USER\Desktop\image-16.jpg'))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
