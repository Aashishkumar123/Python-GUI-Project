from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox,font
from tkinter import ttk
from datetime import datetime
import webbrowser


#======================================================================================
#  ========================== File Code Starts Here  ============================
#=======================================================================================


#=================================== New Code  ======================================
def new():
        text.delete('1.0','end')
#===================================== End =========================================


# ========================= New Window Code  ================================
def new_window():
        root = tk.Tk()
        root.geometry('500x500')


        menubar = Menu(root)

        file = Menu(menubar,tearoff = 0)
        file.add_command(label="New",command=new)
        file.add_command(label="New window",command=new_window)
        file.add_command(label="Open",command=Open)
        file.add_command(label="Save",command=save)
        file.add_command(label="Save as", command=save_as)
        file.add_separator()
        file.add_command(label="Exit",command=exit)
        menubar.add_cascade(label="File",menu=file,font=('verdana',10,'bold'))



        edit = Menu(menubar,tearoff = 0)

        edit.add_command(label="Undo",command=undo)
        edit.add_separator()
        edit.add_command(label="Cut",command=cut)
        edit.add_command(label="Copy",command=copy)
        edit.add_command(label="Paste",command=paste)
        edit.add_command(label="Delete",command=delete)
        edit.add_command(label="Select All",accelerator="Ctrl+A",command=select_all)
        edit.add_command(label="Time/Date",accelerator="F5",command=time)
        menubar.add_cascade(label="Edit",menu=edit)


        Format = Menu(menubar, tearoff = 0)

        Format.add_command(label="Word Wrap")
        Format.add_command(label="Font...", command=fonts)

        menubar.add_cascade(label="Format",menu=Format)



        Help = Menu(menubar, tearoff = 0)

        Help.add_command(label="View Help",command=view_help)
        Help.add_command(label="Send FeedBack",command=send_feedback)
        Help.add_command(label="About Notepad")

        menubar.add_cascade(label="Help",menu=Help)


        root.config(menu=menubar)





        text = ScrolledText(root,width=1000,height=1000)
        text.place(x=0,y=0)



        root.mainloop()

# =========================== End ==============================================        


# ===================== Open File Code ========================================
def Open():
        root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        file = open(root.filename)
        text.insert('end',file.read())
#================================= End ==========================================


#================================ Save File Code ====================================
def save():
        pass
#================================    End      =======================================

#=================================== save as File code  ==============================
def save_as():
        root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
        if root.filename is None:
                return
        file_save =  str(text.get(1.0,END))
        root.filename.write(file_save)
        root.filename.close()
# ================================ End ============================================

# ================================ Exit Code =====================================
def exit():
        message = messagebox.askquestion('Notepad',"Do you want to save changes")
        if message == "yes":
                save_as()
        else:
                root.destroy()
#==================================== end =========================================




#======================================================================================
# ======================= Edit Code Starts Here  ============================
#=======================================================================================

#=========================== Cut code =============================
def cut():
        text.event_generate("<<Cut>>")

#=========================== End code =====================================

#=========================== Cut code =============================
def copy():
        text.event_generate("<<Copy>>")

#=========================== End code =====================================

#=========================== Cut code =============================
def paste():
        text.event_generate("<<Paste>>")

#=========================== End code =====================================


#=========================== Delete all code =============================
def delete():
        message = messagebox.askquestion('Notepad',"Do you want to Delete all")
        if message == "yes":
                text.delete('1.0','end')
        else:
               return "break"

       
#=========================== End code =====================================


#=========================== select all code =============================
def select_all():
        text.tag_add('sel','1.0','end')
        return 'break'
#=========================== End code =============================


#=========================== Time/Date code =============================
def time():
        d = datetime.now()
        text.insert('end',d)
        
#=========================== End code =============================



#======================================================================================
# ======================= Edit Code Ends Here  ============================
#=======================================================================================




#======================================================================================
# ======================= Format Code Starts Here  ============================
#=======================================================================================


def fonts():
        root = tk.Tk()
        root.geometry('400x400')
        root.title('Font')

        l1 = Label(root,text="Font:")
        l1.place(x=10,y=10)
        f = tk.StringVar() 
        fonts = ttk.Combobox(root, width = 15, textvariable = f, state='readonly',font=('verdana',10,'bold'),) 
        fonts['values'] = font.families()
        fonts.place(x=10,y=30)
        fonts.current(0) 


        l2 = Label(root,text="Font Style:")
        l2.place(x=180,y=10)
        st = tk.StringVar() 
        style = ttk.Combobox(root, width = 15, textvariable = st, state='readonly',font=('verdana',10,'bold'),) 
        style['values'] = ('bold','bold italic','italic')
        style.place(x=180,y=30)
        style.current(0) 

        l3 = Label(root,text="Size:")
        l3.place(x=350,y=10)
        sz = tk.StringVar() 
        size = ttk.Combobox(root, width = 2, textvariable = sz, state='readonly',font=('verdana',10,'bold'),) 
        
        size['values'] = (8,9,10,12,15,20,23,25,27,30,35,40,43,47,50,55,65,76,80,90,100,150,200,255,300)
        size.place(x=350,y=30)
        size.current(0) 
               
              
        sample = LabelFrame(root,text="Sample",height=100,width=200)
        sample['font'] = (fonts.get(),size.get(),style.get())
        sample.place(x=180,y=220)

        l4 = Label(sample,text="This is sample")
        l4.place(x=20,y=30)



        def OK():

               text['font'] = (fonts.get(),size.get(),style.get())
               root.destroy()
               

        ok = Button(root,text="OK",relief=RIDGE,borderwidth=2,padx=20,highlightcolor="blue",command=OK)
        ok.place(x=137,y=350)

        def Apl():
                l4['font'] = (fonts.get(),size.get(),style.get())

        Apply = Button(root,text="Apply",relief=RIDGE,borderwidth=2,padx=20,highlightcolor="blue",command=Apl)
        Apply.place(x=210,y=350)        

        def Cnl():
                root.destroy()

        cancel = Button(root,text="Cancel",relief=RIDGE,borderwidth=2,padx=20,command=Cnl)
        cancel.place(x=295,y=350)
        root.mainloop()


#======================================================================================
# ======================= Format Code Ends Here  ============================
#=======================================================================================

#======================================================================================
# ======================= Help Code Ends Here  ============================
#=======================================================================================

# ======================   View Help ===================================
def view_help():
        webbrowser.open('#')

#============================= End =======================================

# ======================   View Help ===================================
def send_feedback():
        webbrowser.open('#')

#============================= End =======================================


#======================================================================================
# ======================= Help Code Ends Here  ============================
#=======================================================================================


# ============================= Main Window =============================

root = tk.Tk()
root.geometry('600x300')
root.minsize(200,100)
root.title('notepad')
root.iconbitmap('notepad.ico')
text = ScrolledText(root,height=1000,undo=True)
text.pack(fill=tk.BOTH)

menubar = Menu(root)

file = Menu(menubar,tearoff = 0)
file.add_command(label="New",command=new)
file.add_command(label="New window",command=new_window)
file.add_command(label="Open",command=Open)
file.add_command(label="Save",command=save)
file.add_command(label="Save as", command=save_as)
file.add_separator()
file.add_command(label="Exit",command=exit)
menubar.add_cascade(label="File",menu=file,font=('verdana',10,'bold'))



edit = Menu(menubar,tearoff = 0)

edit.add_command(label="Undo",accelerator="Ctrl+Z",command=text.edit_undo)
edit.add_command(label="Redo",accelerator="Ctrl+Y",command=text.edit_redo)
edit.add_separator()
edit.add_command(label="Cut",accelerator="Ctrl+X",command=cut)
edit.add_command(label="Copy",accelerator="Ctrl+C",command=copy)
edit.add_command(label="Paste",accelerator="Ctrl+V",command=paste)
edit.add_command(label="Delete",accelerator="Del",command=delete)
edit.add_command(label="Select All",accelerator="Ctrl+A",command=select_all)
edit.add_command(label="Time/Date",accelerator="F5",command=time)
menubar.add_cascade(label="Edit",menu=edit)


Format = Menu(menubar, tearoff = 0)

Format.add_command(label="Word Wrap")
Format.add_command(label="Font...", command=fonts)

menubar.add_cascade(label="Format",menu=Format)



Help = Menu(menubar, tearoff = 0)

Help.add_command(label="View Help",command=view_help)
Help.add_command(label="Send FeedBack",command=send_feedback)
Help.add_command(label="About Notepad")

menubar.add_cascade(label="Help",menu=Help)

# ======================== Right Click Menu =========================================

m = Menu(root, tearoff = 0)
m.add_command(label ="Select All",accelerator="Ctrl+A",command=select_all) 
m.add_command(label ="Cut",accelerator="Ctrl+X",command=cut) 
m.add_command(label ="Copy",accelerator="Ctrl+C",command=copy) 
m.add_command(label ="Paste",accelerator="Ctrl+V",command=paste) 
m.add_command(label ="Delete",accelerator="Del",command=delete) 
m.add_separator() 
m.add_command(label ="Undo",accelerator="Ctrl+Z",command=text.edit_undo)
m.add_command(label ="Redo",accelerator="Ctrl+Z",command=text.edit_redo) 
  
def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
root.bind("<Button-3>", do_popup) 

# ==============================================================================

root.config(menu=menubar)
root.mainloop()

# ========================== End =======================================
