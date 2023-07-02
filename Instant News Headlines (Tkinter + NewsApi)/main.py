
#tkinter module
from tkinter import *

#image module
from PIL import Image, ImageTk

#font from tkinter
from tkinter import font

#requests module
import requests

#random module
import random

#main welcome window code
welcome = Tk()
welcome.title("Sami News ")
welcome.geometry('500x500')

background = Image.open('—Pngtree—vector creative hot news tag_4265321.png')
resized_image = background.resize((500, 500), Image.ANTIALIAS)


#function to open second window
def openSecondWindow():
    selected_optioncountry = ""
    selected_optioncategory=""
    secondwindow = Toplevel()
    secondwindow.title("Select Your Headlines Types")
    secondwindow.geometry("1000x400")
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    langlabel=Label(secondwindow,text="Select Country---US for United States of America",font=bold_font)
    langlabel.pack()

   #saving options select from toggle menu
    def save_option():
        nonlocal selected_optioncountry
        selected_optioncountry= (var.get())[:2]

   #saving options from toggle menu
    def save_option2():
          nonlocal selected_optioncategory
          selected_optioncategory= var2.get()


   #get news api from newsapi
    def getnews():
        api_key = "a8ab6d9bd5684d27bab671e76c15eb91"
        country = selected_optioncountry
        cat= selected_optioncategory
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={cat}&apiKey="+api_key
        news = requests.get(url).json()
        articles = news["articles"]
        my_articles = []
        my_news = ""

        for article in articles:
            my_articles.append(article["title"])

        for i in range(10):
            my_news += f"{i + 1}. {my_articles[i]}\n"

        button_gethealines.config(text=my_news)
    #toggle menu code 1
    var = (StringVar())
    var.set("US-United States of America")
    options = ["GB-Great Britian", "AU-Australia", "FR-France","DE-Germany","RU-Russia","TR-turkey","UA-Ukraine"]
    drop_down = OptionMenu(secondwindow, var, *options)
    drop_down.pack()
    save_button = Button(secondwindow, text="Save Country", command=save_option,width=10,height=1,bg="red",fg="white")
    save_button.place(x=100,y=20)
    save_button.pack()
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    categorylabel=Label(secondwindow,text="Select Category of News",font=bold_font)
    categorylabel.pack()

    #toggle menu code 2
    var2 = (StringVar())
    var2.set("business")
    options = ["sports", "health", "science","technology","general"]
    drop_down2 = OptionMenu(secondwindow, var2, *options)
    drop_down2.pack()
    save_button2 = Button(secondwindow, text="Save Category", command=save_option2,width=10,height=1,bg="red",fg="white")
    save_button2.pack()
    button_gethealines = Button(secondwindow, text="Fetch News",command=getnews)
    button_gethealines.pack()


    secondwindow.mainloop()



#second window of random news generator
def randomwindow():
    randomwindowtab=Toplevel()
    randomwindowtab.title("Random News")
    randomwindowtab.geometry("300x300")

     #get random news by random number generator and countries/categories generated from list
    def randomnews():
        api_key = "a8ab6d9bd5684d27bab671e76c15eb91"
        countries = ['uS','gb', 'au', 'fr', 'de', 'ru', 'tr', 'ua']
        categories = ['science', 'health', 'sports', 'technology', 'general']
        cot = random.randint(0, 7)
        cat = random.randint(0, 4)

        url = f"https://newsapi.org/v2/top-headlines?country={(countries[cot])}&category={(categories[cat])}&apiKey=" + api_key
        news = requests.get(url).json()
        articles = news["articles"]
        my_articles = []
        my_news = ""

        for article in articles:
            my_articles.append(article["title"])
        for i in range(10):
            my_news += f"{i + 1}. {my_articles[i]}\n"
        b3.config(text=my_news)


          #button in this window
    b3 = Button(randomwindowtab,command=randomnews,text="Get Random News Now",activeforeground="red", pady=10, width=20, height=1)
    b3.pack()
    randomwindowtab.mainloop()

#background image
tk_image = ImageTk.PhotoImage(resized_image)
label = Label(welcome, image=tk_image)
label.place(x=0, y=0, relwidth=1, relheight=1)
#button 1
b1 = Button(welcome, command=openSecondWindow, text="Get News Headlines Of Your Choice", activeforeground="red", pady=10, width=30, height=1)
b1.place(x=100,y=90)
#button 2
b2 = Button(welcome, command=randomwindow,text="Get Top10 Random News", activeforeground="red", pady=10, width=20, height=1)
b2.pack(side=BOTTOM)
b1.pack(side=BOTTOM)
bold_font = font.Font(family="Helvetica", size=12, weight="bold")
Welcometext = Label(welcome, text="Get Top Headlines Through News Api", font=bold_font)
Welcometext.pack()


welcome.mainloop()



