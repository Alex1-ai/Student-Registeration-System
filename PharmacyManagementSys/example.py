from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def main():
    master = Tk()
    app = Window1(master)
    master.mainloop()
    #root = Tk()
    #app = Window1(root)
    #root.mainloop()


# creating the secon window
class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management Systems")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()







if __name__ == '__main___':
    main()