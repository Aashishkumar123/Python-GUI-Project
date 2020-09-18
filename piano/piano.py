from tkinter import *
import tkinter as tk
import winsound
from PIL import ImageTk, Image
from playsound import playsound

class piano():

        def button1(self):
                winsound.Beep(1000,100)
        def button2(self):
                playsound('piano11.mp3')
        def button3(self):
                playsound('piano12.mp3')
        def button4(self):
                playsound('piano13.mp3')
        def button5(self):
                playsound('piano14.mp3')
        def button6(self):
                playsound('piano15.mp3')
        def button7(self):
                playsound('piano16.mp3')
        def button8(self):
                playsound('piano17.mp3')
        def button9(self):
                playsound('piano18.mp3')
        def button10(self):
                playsound('piano19.mp3')
        def button11(self):
                playsound('piano110.mp3')
        def button12(self):
                playsound('piano111.mp3')
        def button13(self):
                playsound('piano112.mp3')
        def button14(self):
                playsound('piano113.mp3')
        def button15(self):
                playsound('piano114.mp3')
        def button16(self):
                playsound('piano115.mp3')
        def button17(self):
                playsound('piano116.mp3')
        def button18(self):
                playsound('piano117.mp3')
        def button19(self):
                playsound('piano118.mp3')
        def button20(self):
                playsound('piano119.mp3')
        def button21(self):
                playsound('piano120.mp3')
        def button22(self):
                playsound('piano121.mp3')
        def button23(self):
                playsound('piano122.mp3')


                
        def __init__(self):
                self.root = tk.Tk()
                self.root.geometry('700x300')
                self.root.title("piano")
                self.root.maxsize(700,300)
                self.root.minsize(700,300)
                self.root['bg']="white"

               
                self.icon = ImageTk.PhotoImage(Image.open('piano.png'))

                self.icon_label = Label(self.root,image=self.icon)
                self.icon_label.place(x=295,y=10)

                self.frame1 = Frame(self.root,width=700,height=198,bg="white")
                self.frame1.place(x=0,y=100)

                self.button1 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button1,cursor="hand2")
                self.button1.place(x=0,y=0)
                 
                
                self.button2 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button2,cursor="hand2")
                self.button2.place(x=30,y=0)

                self.button3 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button3,cursor="hand2")
                self.button3.place(x=60,y=0)
                
                self.button4 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button4,cursor="hand2")
                self.button4.place(x=90,y=0)

                self.button5 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button5,cursor="hand2")
                self.button5.place(x=120,y=0)

                self.button6 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button6,cursor="hand2")
                self.button6.place(x=150,y=0)
                
                self.button7 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button7,cursor="hand2")
                self.button7.place(x=180,y=0)

                self.button8 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button8,cursor="hand2")
                self.button8.place(x=210,y=0)
                
                self.button9 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button9,cursor="hand2")
                self.button9.place(x=240,y=0)

                self.button10 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button10,cursor="hand2")
                self.button10.place(x=270,y=0)
                
                self.button11 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button11,cursor="hand2")
                self.button11.place(x=300,y=0)

                self.button12 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button12,cursor="hand2")
                self.button12.place(x=330,y=0)
                
                self.button13 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button13,cursor="hand2")
                self.button13.place(x=360,y=0)

                self.button14 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button14,cursor="hand2")
                self.button14.place(x=390,y=0)
                
                self.button15 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button15,cursor="hand2")
                self.button15.place(x=420,y=0)

                self.button16 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button16,cursor="hand2")
                self.button16.place(x=450,y=0)
                
                self.button17 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button17,cursor="hand2")
                self.button17.place(x=480,y=0)

                self.button18 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button18,cursor="hand2")
                self.button18.place(x=510,y=0)
                
                self.button19 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button19,cursor="hand2")
                self.button19.place(x=540,y=0)

                self.button20 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button20,cursor="hand2")
                self.button20.place(x=570,y=0)
                
                self.button21 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button21,cursor="hand2")
                self.button21.place(x=600,y=0)

                self.button22 = Button(self.frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=self.button22,cursor="hand2")
                self.button22.place(x=630,y=0)
                
                self.button23 = Button(self.frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=self.button23,cursor="hand2")
                self.button23.place(x=660,y=0)



                






                self.root.mainloop()





if __name__ == '__main__':

        piano()
            
    



