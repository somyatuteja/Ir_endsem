import tkinter
from tkinter import *
import twitterstream1

class TwitterGUI(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        titl = Label(text="Twitter Classifier and Summarizer").pack()
        text = Label(text="Enter the query").pack()
        B1 = Button(text="Fetch Tweets", command=self.TweetFetch).pack()
        self.TB1=Entry(top)
        self.TB1.pack()
       # self.summary=Label(text="Summary").grid(row=4, column=2)
        self.summaryTA = Text(top,height=20,width=150)
        self.summaryTA.pack()
        self.summaryTA.insert(1.0, "Summary")

    def TweetFetch(self):
         self.input = self.TB1.get()
         print(self.input)
         ts = twitterstream1.twitterSummary()
         summary=ts.getSummary(self.input)
         self.summaryTA.insert(END,summary)
top = tkinter.Tk()
top.geometry('1650x850+100+100')
app=TwitterGUI(top)
top.mainloop()


