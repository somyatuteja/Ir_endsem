import tkinter
from tkinter import *

class TwitterGUI(Frame):
    def __init__(self):
        top = tkinter.Tk()
        text= Text(top)
        top.lab
        text.insert(INSERT, "ENTER YOUR QUERY")
        text.pack()
        B1=tkinter.Button(text="Fetch Tweets",)
        B1.pack()
        top.mainloop()
    def TweetFetch(self):
