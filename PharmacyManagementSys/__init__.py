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

class Window1:
    def  __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management Systems")
        # height and width of the program
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()








if __name__ == '__main__':
    main()