import tkinter
from tkinter import *
import twitterstream1
import twstream
import tweet3

class TwitterGUI(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        titl = Label(text="TWITTER CLASSIFIER AND SUMMARIZER")
        titl.pack()
        titl.place(x=225, y=10)
        titl.config(font=("Cambiria", 36))
        text = Label(text="Enter the query")
        text.pack()
        text.config(font=("Courier", 20))
        text.place(x=385, y=80)
        B1 = Button(text="Fetch Tweets", command=self.TweetFetch)
        B1.pack()
        B1.place(x=500, y=120)
        B1.config(font=("Courier", 14))
        self.TB1=Entry(top)
        self.TB1.pack()
        self.TB1.place(x=640, y=80)
        self.TB1.config(font=("Courier", 20))
       # self.summary=Label(text="Summary").grid(row=4, column=2)
        self.summaryTA = Text(top,height=28,width=60)
        self.summaryTA.pack()
        self.summaryTA.insert(1.0, "Summary")
        self.summaryTA.place(x=20, y=200)
        self.sentimentTA = Text(top, height=28, width=100)
        self.sentimentTA.pack()
        self.sentimentTA.insert(1.0, "Upcoming Tweets")
        self.sentimentTA.place(x=550, y=200)

    def TweetFetch(self):
         self.input = self.TB1.get()
         print(self.input)
         ts = twstream.twiSummary()
         summary=ts.getSummary(self.input)
         print(summary)
         self.summaryTA.insert(END,summary)
         self.summaryTA.pack
         auth = tweet3.Auth(self.input)
         for num in range(1,20):
            print(num)
            str=tweet3.GetTweetWithSentiment(auth)
            self.sentimentTA.insert(END,str)
            self.summaryTA.pack

top = tkinter.Tk()
top.geometry('1650x850+100+100')
app=TwitterGUI(top)
top.mainloop()


