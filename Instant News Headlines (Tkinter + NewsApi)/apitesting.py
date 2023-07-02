import requests
import tkinter as tk
def getnews():
    api_key="a8ab6d9bd5684d27bab671e76c15eb91"
    url = "https://newsapi.org/v2/top-headlines?country=US&category=business&apiKey="+api_key
    news=requests.get(url).json()
    articles = news["articles"]
    my_articles =[]
    my_news=""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news +  my_articles[i] + "\n"

    label.config(text=my_news)

canvas = tk.Tk()
canvas.geometry("1000x400")
canvas.title("News App")


button=tk.Button(canvas,font =24,text="GetHeadLines",command=getnews)
button.pack(pady = 20)

label=tk.Label(canvas,font = 18,justify = "left")
label.pack(pady =20)

canvas.mainloop()


