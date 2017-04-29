import tkinter
from tkinter import *
import twitterstream1

class TwitterGUI(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        text = Label(text="Enter the query").grid(row=2, column=2)
        B1 = Button(text="Fetch Tweets", command=self.TweetFetch).grid(row=3 ,column=3)
        self.TB1=Entry(top).grid(row=2 ,column=6)


    def TweetFetch(self):
         self.input = self.TB1.get()
         print(self.input)
         ts = twitterstream1.twitterSummary()
         ts.getSummary(self.input)

top = tkinter.Tk()
app=TwitterGUI(top)
top.mainloop()


