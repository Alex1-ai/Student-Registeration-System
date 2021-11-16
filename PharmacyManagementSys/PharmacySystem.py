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





# ===================creating variables for the password and username=========
        self.Username =StringVar()
        self.Password = StringVar()





        # ADDING THE LOGING DETAILS
        # putting the title
        self.LabelTitle = Label(self.frame, text= "Pharmacy Management System",font = ('arial',50, 'bold'), bd=20)
        self.LabelTitle.grid(row= 0, column = 0, columnspan =2 ,pady = 30)


        #====================================FRAMES OF THE DISPLAY=================
        # CREATING THE FRMAES
        self.Loginframe1 = Frame(self.frame, width =1010, height =300, bd=20,relief='ridge')
        # putingthe frames
        self.Loginframe1.grid(row=1,column= 0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=200,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2, column =0)

        self.Loginframe3= Frame(self.frame, width =1000, height =100, bd=20,relief='ridge')

        self.Loginframe3.grid(row=3, column =0, pady=10)


        #=============================LABEL TEXT ============================
        self.lblUsername = Label(self.Loginframe1, text = 'Username',
                                 bd = 22,font=('arial',30,'bold'))
        self.lblUsername.grid(row=0, column =0 )

        self.lblPassword= Label(self.Loginframe1,text = 'Password',bd=22,
                                font= ('arial',30, 'bold'))
        self.lblPassword.grid(row=1, column = 0)

        #==========================Text field==========================
        self.txtUsername = Entry(self.Loginframe1,font =('arial',30,'bold'),
                                 bd = 22, textvariable = self.Username)
        self.txtUsername.grid(row = 0, column =1)
        self.txtPassword = Entry(self.Loginframe1, font = ('arial',30, 'bold'),
                                 bd =22, textvariable = self.Password, show="*")
        self.txtPassword.grid(row=1,column =1,padx = 85)

       #==============================BUTTONS ==============================

        # creating button for the login , reset and exit in frame 2 we have 3 frames
        self.btnLogin =Button(self.Loginframe2,text="Login",width = 17,
                              font = ('arial', 20, 'bold'),
                              command = self.Login_System)
        self.btnLogin.grid(row = 0, column =0)

        self.btnReset= Button(self.Loginframe2,text="Reset",width=17,
                              font = ('arial',20,'bold'), command = self.Reset)
        self.btnReset.grid(row =0, column =1)

        self.btnExit = Button(self.Loginframe2,text="Exit",width=17,
                              font =('arial',20, 'bold'), command=self.iExit)

        self.btnExit.grid(row=0, column=2)



        # to call a the windows we would add a button
        self.btnRegisteration = Button(self.Loginframe3,text = "Patients Registration Systems",
                                       font = ('arial',20, 'bold'),state = DISABLED,command = self.Registeration_window)
        self.btnRegisteration.grid(row = 0, column = 0)

        self.btnHospital = Button(self.Loginframe3, text ="Hospital Management Systems",
                                  font=('arial',20, 'bold'),state = DISABLED,command = self.Hospital_window)
        self.btnHospital.grid(row=0, column= 1,pady = 8, padx = 22)

        #===============LOGIN , RESET, EXIT DETAILS SORTING ====================================
    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if (user == str('Covenant')) and (pas == str('2345')):
            self.btnRegisteration.config(state= NORMAL)
            self.btnHospital.config(state= NORMAL)
        else:
                # adding messagebox
            tkinter.messagebox.askyesno("Pharmacy Management System", "You have entered an invalid Login detials, Try again")
            self.btnRegisteration.config(state = DISABLED)
            self.btnHospital.config(state = DISABLED)
            self.Username.set("")
            self.Password.set("")
                # putting the cursor on the username
            self.txtUsername.focus()

    def Reset(self):
        self.btnRegisteration.config(state=DISABLED)
        self.btnHospital.config(state = DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Confirm if you want to exit")

        if self.iExit > 0:
            self.master.destroy()
        return


#================================================================================

    # creating function to put all the the three window
    # using these functions to call new Window1
    def Registeration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    # for the second the window
    # These function for the secon window
    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)


# switches to patient registeration system
class Window2:
    def  __init__(self, master):
        self.master = master
        self.master.title("Patients Registeration Systems")
        # height and width of the program
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


# The second window for the Hospital Management Systems
class Window3:
    def  __init__(self, master):
        self.master = master
        self.master.title("Hospital Management Systems")
        # height and width of the program
        self.master.geometry('1350x750+0+0')
        self.master.configure(background='powder blue')

        #=================================INITIALIZING THE VARIABLES==================================================
        cmbNameTablets=StringVar()
        Ref = StringVar()
        Dose=StringVar()
        NumberTablest=StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpDate=StringVar()
        DailyDose=StringVar()
        PossibleSideEffects=StringVar()
        FurtherInformation=StringVar()
        StorageAdvice=StringVar()
        DrivingUsingMachines=StringVar()
        HowtoUseMedication=StringVar()
        PatientID = StringVar()
        PatientNHSNo=StringVar()
        PatientName=StringVar()
        PatientBirth = StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()

        #=====================================CREATING  FRAMES===================================================================


        """self.frame = Frame(self.master)
        self.frame.pack()"""
        MainFrame= Frame(self.master)
        MainFrame.grid()



        #initializing the title Frame
        TitleFrame= Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 40, 'bold'), text="Hospital Management Systems", padx=2)
        self.lblTitle.grid()



        FrameDetail = Frame(MainFrame, bd=20, width=1350,height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)


        # packing them into the dataframe to left right and bottom
        DataFrame = Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = Frame(DataFrame, bd=10, width=800, height=400, padx=20, relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = Frame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)


       # creating a lable for the dataframe box
        self.lblNameTablet= Label(DataFrameLEFT, font=('arial',12, 'bold'), text="Name of Tablets", padx=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

       # for combo box
        self.cboNameTablet= ttk.Combobox(DataFrameLEFT, textvariable=  cmbNameTablets, state='readonly',font=('arial',12,'bold'),
                                        width=20)
        self.cboNameTablet['value'] = ('', 'Ibuprofen', 'Co-codamol',
                                      'Paracetamol','Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        # creating a lable for the dataframe box
        self.lblFurtherInfo = Label(DataFrameLEFT, font=('arial', 12, 'bold'),
                                   text="Further Information:", padx=2)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),
                                    textvariable=FurtherInformation)
        self.txtFurtherInfo.grid(row=0, column=3)



        # creating a lable for the dataframe box
        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'),
                                    text="Reference No:", padx=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),
                                    textvariable=Ref)
        self.txtRef.grid(row=1, column=1)



        # creating a lable for the dataframe box
        self.lblStorage= Label(DataFrameLEFT, font=('arial', 12, 'bold'),
                                    text="Storage Advice:", padx=2)
        self.lblStorage.grid(row=1, column=2, sticky=W)
        self.lblStorage = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),
                                    textvariable=StorageAdvice)
        self.lblStorage.grid(row=1, column=3)



if __name__ == '__main__':
    main()