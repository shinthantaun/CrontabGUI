from tkinter import *
from tkinter import ttk

def saveCron():
    print("Saved Cron!")
    pass

class View:

    def __init__(self, windowSize):
        
        # Create main app
        self.app = Tk()
        self.app.title("Cronjob Manager")
        self.app.geometry(windowSize)
        self.app.resizable(False, False)

        # Read on/off photo
        try:
            self.on = PhotoImage(file="on.png")
            self.off = PhotoImage(file="off.png")
        except:
            print("Cannot open images!\n")

        # Create Canvas
        self.canvas = Canvas(self.app
                    , bg="#EFF5F5"
                    , width=510
                    , height=500)
        self.canvas.grid(column=0)
        
        # Create Scrollbar
        self.scrollbar = Scrollbar(self.app
                    , orient='vertical'
                    , command=self.canvas.yview)
        self.scrollbar.grid(row=0,column=2,sticky=NS)
 
        # Bind Canvas with Scrollbar 
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>'
            , lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.frame = Frame(self.canvas)
        self.canvas.create_window((0,0),window=self.frame,anchor="nw")

        self.status = [] #Change later

    def _toggle(self, button, row):

        if self.status[row]:#Change later
            button.config(image=self.off)
            self.status[row] = False 
        else:
            button.config(image=self.on)
            self.status[row] = True #Change later

    def createButton(self, instantNo, jobName, status):
        
        # Create label using cronjob command
        cronJob = ttk.Label(self.frame
                , text=jobName
                , width=45
                , anchor="w"
                , borderwidth=1
                , relief="solid")

        cronJob.grid(row=instantNo, column=0
                , ipadx=10, ipady=10
                , padx = 3, pady=3)
        
        cronJob.config(font=('Georgia', 10)
                    ,foreground="#497174"
                    ,background='#D6E4E5'
                    )
        
        # Set on/off button
        img = self.off
        self.status.insert(instantNo, status) #Change later
        if (status):
            img = self.on

        # Create button
        button = ttk.Button(self.frame
                            , image=img
                            , width=50
                            , command=lambda: self._toggle(button, instantNo))

        button.grid(row=instantNo, column=1
                    , ipadx=5, ipady=5
                    , padx=3 , pady=3
                    ,sticky='e')
           
    def runView(self, dummycron): #Change later
        
        for index, cronjob in enumerate(dummycron): 
            jobName = cronjob[0]
            status = cronjob[1]
            self.createButton(index, jobName, status)

        # Create save button    
        save = Button(self.app
                    , text ="Save"
                    , width=10,height=2
                    ,command=saveCron)
        save.grid(row=1
                    , ipadx=3, ipady=3
                    , padx=3 , pady=3)
        save.config(font=('Georgia', 10)
                    ,foreground="#FFEFEF"
                    ,background='#1A374D'
                    ,border=0
                    )