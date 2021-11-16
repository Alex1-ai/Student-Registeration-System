from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time
import datetime


def main():
    root = Tk()
    app = Window1(root)
    # master.mainloop()


# creating the secon window
class Window1:
    def __init__(self, master):
        self.master = master
        # given the title
        self.master.title("Pharmacy Management Systems")
        # checking the size of the window
        self.master.geometry('1350x750+0+0')
        # creating a frame
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == "__main___":
    main()