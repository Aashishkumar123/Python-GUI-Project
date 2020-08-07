import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
root = tk.Tk()
root.geometry('500x300')
root.maxsize(500,300)
root.minsize(500,300)
root.title('Send SMS')
root.iconbitmap('Sms.ico')

def send_sms():
        number = phone_no.get()
        messages = message.get("1.0","end-1c")

        url = "https://www.fast2sms.com/dev/bulk"
        api = "put your api here" #Go to fast2sms.com and signup to get the free Api
        querystring = {"authorization":api,"sender_id":"FSTSMS","message":messages,"language":"english","route":"p","numbers":number}

        headers = {
                 'cache-control': "no-cache"
                 }
        requests.request("GET", url, headers=headers, params=querystring)
        messagebox.showinfo("Send SMS",'SMS has been send successfully')


        






img = ImageTk.PhotoImage(Image.open('background.jpg'))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


label = Label(root,text="Send SMS Using Python",font=('verdana',10,'bold'))
label.place(x=210,y=10)

phone_no = Entry(root,width=20,borderwidth=0,font=('verdana',10,'bold'))
phone_no.place(x=220,y=115)
phone_no.insert('end','phone number')

message = Text(root,height=5,width=25,borderwidth=0,font=('verdana',10,'bold'))
message.place(x=190,y=140)
message.insert('end','Message')

send = Button(root,text="Send Message",font=('verdana',10,'bold'),relief=RIDGE,cursor='hand2',borderwidth=0,command=send_sms)
send.place(x=260,y=235)
root.mainloop()
