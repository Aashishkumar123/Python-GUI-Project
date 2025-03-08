# Inspirado no programa 'clac1.py' do livro "Python and Tkinter Programming" de John E.Grayson
from tkinter import *

def frame(root, side):
    w = Frame(master=root)
    w.pack(side=side, expand=True, fill=BOTH, padx=(5, 0))
    return w

def button(root, text, side, command=None, **kw):
    w = Button(master=root, text=text,
               command=command, relief=RIDGE, **kw)
    w.pack(side=side, expand=True, fill=BOTH)
    return w

root = Frame()
display = StringVar()
frame_top = Frame(root,)
frame_top.pack(side=TOP, fill=BOTH, expand=YES)
Entry(master=frame_top, relief=SUNKEN,
      textvariable=display).pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=2)
Button(frame_top, text="C",
       command=lambda w=display: w.set(''),
       bg="red", fg="white", relief=RIDGE).pack(side=RIGHT, expand=False, padx=2)


for i in "987+ 654- 321* 0d./".split():
    frame2buttons = frame(root, TOP)
    for char in i:
        if char == "d":
            button(frame2buttons, "00", LEFT,
                   lambda w=display: w.set(w.get()+"00"))
        else:
            
            button(frame2buttons,char,LEFT,
                   lambda w=display, c='%s' % char: w.set(w.get()+c))


def result(w, e=None):
    s = w.get()
    if '%' in s:
        index = list(s).index('%')
        list_s = list(s)
        list_s.insert(0, '(')
        list_s.insert(index+1, ')/100')
        list_s[index+2] = '*'
        s = ''.join(list_s)
        
    w.set(eval(s))

frame_bottom = frame(root, BOTTOM)
button(frame_bottom, "=", LEFT, command=lambda w=display: result(w), bg="red", fg="white")
Button(master=frame_bottom, text="%", relief=RIDGE, command=lambda w=display: w.set(w.get()+"%")).pack(side=LEFT, expand=False)

root.pack(side=TOP, fill=BOTH, expand=True)
root.mainloop()
