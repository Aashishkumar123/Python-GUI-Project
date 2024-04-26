from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image 
from tkinter import messagebox
import smtplib
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()

# Custom styles for hover effects
style = ttk.Style()
style.theme_use('clam')  # You can choose a different theme if needed

style.map("C.TButton",
    foreground=[('pressed', 'black'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'gray'), ('active', 'white')]
)

style.map("L.TButton",
    foreground=[('pressed', 'black'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'gray'), ('active', 'orange')]
)

def on_enter(event):
    event.widget.config(bg="orange")

def on_leave(event):
    event.widget.config(bg="white")

def Login():
    e = email.get()
    p = password.get() 

    if '@gmail.com' not in e or e == "":
        messagebox.showerror('Login error',"Please write a valid email")
    elif p == "":
        messagebox.showerror('Login error',"Password shouldn't be empty")
    else:
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls()
            s.login(e,p)
            messagebox.showinfo("Login Success","You have logged into Gmail successfully")
            root.withdraw()  # Hide login window
            
            # Create the main window
            main_window = tk.Toplevel()
            main_window.geometry('500x400')
            main_window.title('Email Sender')
            
            def Logout():
                s.quit()
                main_window.destroy()

            header1 = Label(main_window, bg="orange", width=300, height=2)
            header1.place(x=0, y=0)

            h2 = Label(main_window, text="Email Sender", bg="orange", fg="black", font=('verdana', 13, 'bold'))
            h2.place(x=175, y=5)
            
            logout = ttk.Button(main_window, text="Logout", style="C.TButton", width=10, command=Logout)
            logout.place(x=390, y=38)

            r = Label(main_window, text="Recipient Email Address", font=('verdana', 10, 'bold'))
            r.place(x=130, y=130)
            recipient = Entry(main_window, width=30, relief=RIDGE, borderwidth=3)
            recipient.place(x=130, y=150)

            st = Label(main_window, text="Subject", font=('verdana', 10, 'bold'))
            st.place(x=130, y=190)
            subject = Entry(main_window, width=30, relief=RIDGE, borderwidth=3)
            subject.place(x=130, y=210)

            m = Label(main_window, text="Message", font=('verdana', 10, 'bold'))
            m.place(x=130, y=250)

            message = ScrolledText(main_window, width=40, height=5, relief=RIDGE, borderwidth=3)
            message.place(x=130, y=270)

            def Send():
                r = recipient.get()
                st = subject.get()
                m = message.get('1.0', END)

                if '@gmail.com' not in r or r == "":
                    messagebox.showerror('Sending Mail error', "Please write a valid email")
                elif m == "":
                    messagebox.showerror('Sending Mail error', "Message shouldn't be empty")
                else:
                    s.sendmail(r, e, f'Subject :{st}\n\n {m}')
                    messagebox.showinfo("Success", "Your message has been sent successfully")

            send = ttk.Button(main_window, text="Send", style="C.TButton", width=10, command=Send)
            send.place(x=350, y=360)

            main_window.mainloop()

        except:
            messagebox.showerror('Login error', "Failed to login. Check your email or password.")

root.title('Email Sender')
root.geometry('400x300')
root.maxsize(400,300)
root.minsize(400,300)

header = Label(root, bg="orange", width=300, height=2)
header.place(x=0, y=0)

h1 = Label(root, text="Email Sender", bg="orange", fg="black", font=('verdana', 13, 'bold'))
h1.place(x=135, y=5)

img = ImageTk.PhotoImage(Image.open('gmail.png'))

logo = Label(root, image=img, borderwidth=0)
logo.place(x=150, y=38)

e = Label(root, text="Email Address", font=('verdana', 10, 'bold'))
e.place(x=100, y=130)
email = Entry(root, width=30, relief=RIDGE, borderwidth=3, font=('Arial', 10))  # Changed font here
email.place(x=100, y=150)
email.bind("<Enter>", on_enter)
email.bind("<Leave>", on_leave)

p = Label(root, text="Password", font=('verdana', 10, 'bold'))
p.place(x=100, y=190)
password = Entry(root, width=30, relief=RIDGE, borderwidth=3, font=('Arial', 10))  # Changed font here
password.place(x=100, y=210)
password.bind("<Enter>", on_enter)
password.bind("<Leave>", on_leave)

login = ttk.Button(root, text="Login", style="L.TButton", width=10, command=Login)  # Changed style here
login.place(x=145, y=240)

root.mainloop()
