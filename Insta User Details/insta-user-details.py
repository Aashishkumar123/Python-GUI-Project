from tkinter import *
import tkinter as tk
import requests

root = tk.Tk()
root.title("Instagram User Details")
root.geometry('400x300')



def search():
        u_name = user.get()
        url = f"https://www.instagram.com/{u_name}/?__a=1"
        
        data = requests.get(url).json()
        print(data)



        def pic():
                import webbrowser
                d = data['graphql']['user']['profile_pic_url']
                webbrowser.open(d)


        if details.get(1.0,END) != "":
                details.delete(1.0,END)
                details.insert(1.0,f"\t username : {data['graphql']['user']['username']} \n     followers : {data['graphql']['user']['edge_followed_by']['count']}      following : {data['graphql']['user']['edge_follow']['count']} \n   full name : {data['graphql']['user']['full_name']} \n Total post : {data['graphql']['user']['edge_owner_to_timeline_media']['count']}  category : {data['graphql']['user']['category_enum']} \n        Email : {data['graphql']['user']['business_email']} \nbio-link:{data['graphql']['user']['external_url']}private account:{data['graphql']['user']['is_private']} || verified account:{data['graphql']['user']['is_verified']}  bussiness account:{data['graphql']['user']['is_business_account']}  \n \n   see profile picture" )



                Button(innerframe1,text="click to see",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=pic).place(x=180,y=145)



        


        
        





frame = Frame(root,width=400,height=300,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame.place(x=0,y=0)

innerframe = LabelFrame(frame,width=380,height=50,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe.place(x=5,y=5)


user = Entry(frame,width=30,relief=RIDGE,borderwidth=3)
user.place(x=70,y=15)

search = Button(frame,text="Search",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=search)
search.place(x=270,y=15)


innerframe = LabelFrame(frame,width=380,height=240,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe.place(x=5,y=45)


innerframe1 = LabelFrame(innerframe,text="Users Details",width=370,height=230,highlightbackground="white", highlightcolor="white", highlightthickness=5,font=('verdana',10,'bold'))
innerframe1.place(x=0,y=0)


details = Text(innerframe1,height=12,width=47,relief=RIDGE,borderwidth=5,highlightbackground="white", highlightcolor="white",font=('courier',9,''))
details.place(x=5,y=5)

root.mainloop()