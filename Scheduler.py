'''
Author : Bishal jaiswal
Date   : Wednesday, April 27, 2022
purpose: To schedule the works to do later

------ Module used --------
# tkinter --> message box
# datetime

'''

from tkinter import *
from datetime import date
from datetime import datetime
from tkinter import messagebox as msg
from tkinter import filedialog


# getting the full date
today = date.today()
full_date= today.strftime("%B, %d %Y")
# ---------------------------------------

# getting the time today
time_today = datetime.now()
Time = time_today.strftime("%I:%M:%S") 

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("930x500")
        self.title("Scheduler -By Bishal jaiswal")
        self.iconbitmap("scheduler.ico")
        self.configure(background="#8ECCF6")
        self.resizable(False,False)
        
        self.welcome_frame = Frame(self,bg='#8ECCF6')
        self.welcome_frame.pack()
        
        wlc_label = Label(self.welcome_frame, text="Hello welcome To Scheduler!",font="cambria 20 bold",bg='#8ECCF6')
        wlc_label.pack()
        
        date_label = Label(self.welcome_frame,text=f"{full_date}",font="Arial 9 bold",background="#8ECCF6")
        date_label.pack()
        
        schedule_area = LabelFrame(self,text="Schedule Area",bg='#8ECCF6',font="Lucida 10 bold",relief=GROOVE,bd=6)
        schedule_area.place(x=5,y=70,width=500,height=400)

        # Task area
        task_area = LabelFrame(self,text="Scheduled Tasks",bg='#8ECCF6',font="Lucida 10 bold",relief=GROOVE,bd=6)
        task_area.place(x=520,y=70,width=400,height=400)

        # ----------- Text area & scrollbar ------------

        scroll = Scrollbar(task_area,orient=VERTICAL)
        tasks = Text(task_area,yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=tasks.yview)
        tasks.pack(fill=BOTH,anchor=N)


        
        
        # -------- variable of Entry --------------------

        work_var = StringVar()
        time_var = StringVar()
        name_var = StringVar()
        contact_var = StringVar()
        job_var = StringVar()

        # ----------- Label inside LabelFrame starts ---------------
        schedule_work_label = Label(schedule_area, text="Schedule (work)        :",bg="white",background='#8ECCF6',font="cambria 13 bold")
        schedule_work_label.place(x=1,y=5)

        schedule_time_label = Label(schedule_area, text="Schedule To (Time)  :",bg="white",background='#8ECCF6',font="cambria 13 bold")
        schedule_time_label.place(x=1,y=50)

        schedule_time_label = Label(schedule_area, text="Your Name                  :",bg="white",background='#8ECCF6',font="cambria 13 bold")
        schedule_time_label.place(x=1,y=100)

        schedule_time_label = Label(schedule_area, text="Your Contact No.       :",bg="white",background='#8ECCF6',font="cambria 13 bold")
        schedule_time_label.place(x=1,y=150)

        schedule_time_label = Label(schedule_area, text="Your Job (optional)  :",bg="white",background='#8ECCF6',font="cambria 13 bold")
        schedule_time_label.place(x=1,y=200)
        
        Label(schedule_area, text="- By Bishal jaiswal",background='#8ECCF6',font="Lucida 9 bold").place(x=379,y=350)
        # ----------- Label inside LabelFrame ends here -------------

        # ----------- Label Entry --------------
        work_label_entry = Entry(schedule_area, font="cambria 10 bold",textvariable=work_var,relief=SUNKEN,bd=3)
        work_label_entry.place(x=200,y=10)

        time_label_entry = Entry(schedule_area, font="cambria 10 bold",textvariable=time_var,relief=SUNKEN,bd=3)
        time_label_entry.place(x=200,y=55)

        name_label_entry = Entry(schedule_area, font="cambria 10 bold",textvariable=name_var,relief=SUNKEN,bd=3)
        name_label_entry.place(x=200,y=105)

        contact_label_entry = Entry(schedule_area, font="cambria 10 bold",textvariable=contact_var,relief=SUNKEN,bd=3)
        contact_label_entry.place(x=200,y=150)

        job_label_entry = Entry(schedule_area, font="cambria 10 bold",textvariable=job_var,relief=SUNKEN,bd=3)
        job_label_entry.place(x=200,y=205)

        #  ---------------- Buttons -save,reset -----------
        # ----------- Button functions -----------


        def saveFile():
            doneWork()
            try:
                path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[
                                                        ("Text File",".txt"),
                                                        ("All Files","*.*"),
                                                        ("HTML File",".html"),
                                                        ("Ms-Word",".docs")
                                                            ])
                with open(path,"w") as file:
                    file.write(tasks.get(1.0,END))
                    msg.showinfo("Saved","File saved successfully")            
            except Exception as e:
                return e

        def clearData():
            ask_to_clear = msg.askyesno("Reset","Are you sure to reset the data?")
            if ask_to_clear>0:
                work_var.set("")
                time_var.set("")
                name_var.set("")
                contact_var.set("")
                job_var.set("")
                doneWork()
                msg.showinfo("Data","Data cleared successfully :D")
            return clearData

        def doneWork():
            tasks.delete(1.0,END)
            tasks.insert(END,"\t-------- Your Tasks Here --------\n")
            tasks.insert(END,f"\n  Name          : {name_var.get()}")
            tasks.insert(END,f"\n  Contact       : {contact_var.get()}")
            tasks.insert(END,f"\n  Schedule work : {work_var.get()}")
            tasks.insert(END,f"\n  Schedule Time : {time_var.get()}")
            tasks.insert(END,f"\n  Job           : {job_var.get()}")
        doneWork()

        def exitApp():
            ask_for_exit=msg.askyesno("Exit","Are you sure to exit?")
            if ask_for_exit>0:
                self.destroy()

        def openFile():
            work_var.set("")
            time_var.set("")
            name_var.set("")
            contact_var.set("")
            job_var.set("")
            doneWork()
                   
            try:
                path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[
                    ("Text File",".txt"),
                    ("Ms-word File",".docs"),
                    ("All Files","*.*")
                    ])
                with open(path,"r") as file:
                    content = file.read()
                    tasks.delete(1.0,END)
                    tasks.insert(END,content)
            except Exception as e:
                return e


        # functions of the buttons ends here
        
        saveButton = Button(schedule_area, text="Save",font="Arial 12 bold",relief=GROOVE,bg="#8ECCF6",bd=6,width=5,command=saveFile)
        saveButton.place(x= 10,y=330)

        doneButton = Button(schedule_area, text="Done",font="Arial 12 bold",relief=GROOVE,bg="#8ECCF6",bd=6,command = doneWork)
        doneButton.place(x= 88,y=330)

        resetButton = Button(schedule_area, text="Reset",font="Arial 12 bold",relief=GROOVE,bg="#8ECCF6",bd=6,command = clearData)
        resetButton.place(x= 168,y=330)

        exitButton = Button(schedule_area, text="Exit",font="Arial 12 bold",relief=GROOVE,bg="#8ECCF6",bd=6,command = exitApp)
        exitButton.place(x= 250,y=330)

        openButton = Button(schedule_area, text="Open",font="Arial 12 bold",relief=GROOVE,bg="#8ECCF6",bd=6,command = openFile)
        openButton.place(x= 315,y=330)




if __name__ == "__main__":
    root = App()
    root.mainloop()