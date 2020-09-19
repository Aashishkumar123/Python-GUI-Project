from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from playsound import playsound
root = tk.Tk()
root.geometry('700x300')
root.title("piano")
root.maxsize(700,300)
root.minsize(700,300)
root['bg']="white"
icon = ImageTk.PhotoImage(Image.open('piano.png'))
icon_label = Label(root,image=icon)
icon_label.place(x=295,y=10)
frame1 = Frame(root,width=700,height=198,bg="white")
frame1.place(x=0,y=100)
class piano():
        def PianoSound(self,sound):
                playsound(f'Piano{sound}.mp3')
        def __init__(self,index):
                self.index = index
                if self.index%2 != 0:
                        Button(frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=lambda:self.PianoSound(self.index),cursor="hand2").grid(row=0,column=self.index)
                else:
                        Button(frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=lambda:self.PianoSound(self.index),cursor="hand2").grid(row=0,column=self.index)
if __name__ == '__main__':
        for i in range(1,24):
                piano(i)
root.mainloop()    
    



