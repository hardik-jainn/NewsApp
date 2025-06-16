import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
class NewsApp:

    def __init__(self):

        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=d01e39a93fc54e09bf91a9df57bb293a').json()
        # Load initial GUI
        self.load_gui()
        # Load the 1st news
        self.load_news_item(0)
    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.config(bg='black')
        self.root.title('My News App')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):
        # clear the screen for new news item
        self.clear()

        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img)
        except:
            img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Image_not_available.png/640px-Image_not_available.png'
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(img)
        label = Label(self.root,image=photo)
        label.pack()
        heading = Label(self.root,text=self.data['articles'][index]['title'],
                        fg='white',bg='black',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root, text=self.data['articles'][index]['description'],
                        fg='white', bg='black', wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text='PREV',width=16,height=3,command=lambda : self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='READ MORE', width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='NEXT', width=16, height=3,
                          command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)
obj = NewsApp()
