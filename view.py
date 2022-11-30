from tkinter import *
from tkinter import ttk
import constants
import crontab


class View:

    def __init__(self):
        
        # Create main app
        self.app = Tk()
        self.app.title("Cronjob Manager")
        self.app.geometry(constants.app['windowSize'])
        self.app.resizable(False, False)

        # Read on/off photo
        try:
            self._on = PhotoImage(file="on.png")
            self._off = PhotoImage(file="off.png")
        except:
            print("Cannot open images!\n")
            exit()

        # Create _canvas
        self._canvas = Canvas(self.app
                    , bg= constants.canvas['background']
                    , width=510
                    , height=500)
        self._canvas.grid(column=0)
        
        # Create _scrollbar
        self._scrollbar = Scrollbar(self.app
                    , orient='vertical'
                    , command=self._canvas.yview)
        self._scrollbar.grid(row=0,column=2,sticky=NS)
 
        # Bind _canvas with _scrollbar 
        self._canvas.configure(yscrollcommand=self._scrollbar.set)
        self._canvas.bind('<Configure>'
            , lambda e: self._canvas.configure(scrollregion=self._canvas.bbox("all")))
        self._frame = Frame(self._canvas)
        self._canvas.create_window((0,0),window=self._frame,anchor="nw")

        self.status = [] #Change later

    def _toggle(self, button, row):

        if self.status[row]:#Change later
            button.config(image=self._off)
            self.status[row] = False 
        else:
            button.config(image=self._on)
            self.status[row] = True #Change later

    def _createButton(self, instantNo, jobName, status):
        
        # Create label using cronjob command
        cronJob = ttk.Label(self._frame
                , text=jobName
                , width=45
                , anchor="w"
                , borderwidth=1
                , relief="solid")

        cronJob.grid(row=instantNo, column=0
                , ipadx=10, ipady=10
                , padx = 3, pady=3)
        
        cronJob.config(font=('Georgia', 10)
                    ,foreground=constants.cronJob['fontcolor']
                    ,background=constants.cronJob['background']
                    )
        
        # Set on/off button
        img = self._off
        self.status.insert(instantNo, status) #Change later
        if (status):
            img = self._on

        # Create button
        button = ttk.Button(self._frame
                            , image=img
                            , width=50
                            , command=lambda: self._toggle(button, instantNo))

        button.grid(row=instantNo, column=1
                    , ipadx=5, ipady=5
                    , padx=3 , pady=3
                    ,sticky='e')
          
    def run(self, dummycron): #Change later
        
        for index, cronjob in enumerate(dummycron): 
            jobName = cronjob[0]
            status = cronjob[1]
            self._createButton(index, jobName, status)

        # Create save button    
        save = Button(self.app
                    , text ="Save"
                    , width=10
                    ,command=crontab.saveCron)
        save.grid(row=1
                    , ipadx=3, ipady=3
                    , padx=3 , pady=10)
        save.config(font=('Georgia', 10)
                    ,foreground=constants.saveButton['fontcolor']
                    ,background=constants.saveButton['background']
                    ,border=0
                    )

def runView(dummycron):
    view = View()
    view.run(dummycron)
    view.app.mainloop()