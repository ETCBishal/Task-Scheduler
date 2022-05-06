'''
auth_Name: Bishal jaiswal
DATE : Thursday, April 28, 2022
Project_Name : Contact Manager 

---------- Module userd ----------
tkinter
pymysql
datetime
'''

from tkinter import *
from tkinter import messagebox as mes
import pymysql as db
from datetime import date,datetime
from tkinter import ttk

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Manager")
        self.geometry("1000x380")
        # self.resizable(False,False)
        self.configure(background="#25CBEC")
        self.iconbitmap("contact.ico")


        # variables

        today = date.today()
        now = datetime.now()
        contact_number_var = StringVar()
        contact_name_var = StringVar()
        gender_var = StringVar()
        email_var = StringVar()
        # -----------------------------
        def preView():
            if contact_number_var.get() != "" and contact_name_var.get() !="" or email_var.get() !="":
                try:
                    con = db.connect(host="localhost",password="",user="root",database="ContactManager") 
                    cur = con.cursor()
                    cur.execute("insert into contacts(S_NO,contact_number,contact_name,Gender,Email,date,Time)values(%s,%s,%s,%s,%s,%s,%s)",
                    ("",
                    contact_number_var.get(),
                    contact_name_var.get(),
                    gender_var.get(),
                    email_var.get(),
                    today.strftime("%d/%m/%Y"),
                    now.strftime("%I:%M:%S")))
                    con.commit()
                    con.close()
                    
                    mes.showinfo("Conform","Successfull")
                except Exception as e:
                    mes.showerror("Error",f"Error: {e}")
        
        welcome_frame = Frame(self,pady=15,bg="#25CBEC")
        welcome_frame.pack(side=LEFT,anchor=N,padx=35)

        welc_label = Label(welcome_frame, text="Contact Manager",font="Times 24 bold",bg="#25CBEC")
        welc_label.pack(padx=30)

        # Creating the labels
        contactFrame = LabelFrame(self,text="Save Contacts", font="cambria 10 bold",bg="#25CBEC",bd=6)
        contactFrame.place(x=15,y=70,width=350,height=280)

        contact_number = Label(contactFrame, text="Contact Number. :",font="Times 12 bold",bg="#25CBEC")
        contact_number.place(x=5,y=30)

        contact_name = Label(contactFrame, text="Contact Name      :",font="Times 12 bold",bg="#25CBEC")
        contact_name.place(x=5,y=78)

        gender = Label(contactFrame, text="Gender  :",font="Times 12 bold",bg="#25CBEC")
        gender.place(x=5,y=125)

        email = Label(contactFrame, text="Email (Optional)  :",font="Times 12 bold",bg="#25CBEC")
        email.place(x=5,y=170)


        # Creating entry of the label above
        contact_number_entry = Entry(contactFrame,bd=3,relief=SUNKEN,font="Times 12 bold",textvariable=contact_number_var)
        contact_number_entry.place(x=140,y=30)

        contact_name_entry = Entry(contactFrame,bd=3,relief=SUNKEN,font="Times 12 bold",textvariable=contact_name_var)
        contact_name_entry.place(x=140,y=78)

        combo_gender = ttk.Combobox(contactFrame,font="Times 10 bold",state='readonly',textvariable=gender_var)
        combo_gender['values'] = ("Male","Female","Others")
        combo_gender.place(x=140,y=125)

        email_entry = Entry(contactFrame,bd=3,relief=SUNKEN,font="Times 12 bold",textvariable=email_var)
        email_entry.place(x=140,y=170)

        # creating button --> conform
        conformButton = Button(contactFrame, text="Save",font="lucida 9 bold",relief=GROOVE, bd=6,bg="#25CBEC",command=preView,width=5)
        conformButton.place(x=265, y=215)



if __name__ == "__main__":
    root = GUI()
    root.mainloop()
