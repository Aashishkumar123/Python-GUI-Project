import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pytube
import time

root = tk.Tk()
root.title("Youtube Downloader")
root.iconbitmap("Youtube.ico")
root.geometry("700x300")
#root.maxsize(700,250)
root.minsize(700,300)


def download():
        link = text.get("1.0","end-1c")

        if link == '':
                messagebox.showerror("YouTube Downloader", "Please paste a link here") 
        else:
                yt = pytube.YouTube(link)
                stream = yt.streams.first()
                time.sleep(2)
                text.delete(1.0,'end') 
                text.insert('end','Wait Downloading ......')
                time.sleep(5)
                stream.download()
                messagebox.showinfo("YouTube Downloader",'Video has been download successfully')


        


header = Label(root,bg="black",width="300",height="2")
header.place(x=0,y=0)

yt_logo = ImageTk.PhotoImage(Image.open('youtube.png'))
logo = Label(root, image = yt_logo,borderwidth=0)
logo.place(x=10,y=10)

caption = Label(root,text="YouTube Downloader",font=('verdana',10,'bold'))
caption.place(x=50,y=10)



yt1_logo = ImageTk.PhotoImage(Image.open('yt.png'))
logo1 = Label(root, image = yt1_logo,borderwidth=0)
logo1.place(x=300,y=60)


text = Text(root,width=60,height=2,font=('verdana',10,'bold'))
text.place(x=90,y=180) 
text.insert('end','Paste your video link here')

button = Button(root,text="Download",relief=RIDGE,font=('verdana',10,'bold'),bg="red",fg="white",command=download)
button.place(x=330,y=220)
root.mainloop()