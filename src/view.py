from tkinter import *
from tkinter import ttk
import settings

class View:

    def __init__(self)->object:
        """
        GUI View Class to turn on/off cronjobs
        
        Exceptions:
            Raise Error: Cannot open images!
        """
        # Create main app
        self.app = Tk()
        self._jobs = {}
        self.app.title("Cronjob Manager")
        self.app.geometry(settings.app['windowSize'])
        # self.app.configure(background=settings.canvas['background'])
        # self.app.resizable(False, False)
        # Read on/off photo
        try:
            self._on = PhotoImage(file= settings.imgpath + "on.png")
            self._off = PhotoImage(file= settings.imgpath + "off.png")
            self._logo = PhotoImage(file= settings.imgpath + "logo.png")
        except:
            print("Error: Cannot open images!")
            self.app.destroy()
            exit()
        self.app.iconphoto(True,self._logo)
        # Create _canvas
        self._canvas = Canvas(self.app
                    , bg= settings.canvas['background']
                    , width=780
                    , height=500)
        self._canvas.grid(column=0)
        # Create _scrollbar
        self._scrollbar = Scrollbar(self.app
                    , orient='vertical'
                    , command=self._canvas.yview)
        self._scrollbar.grid(row=0,column=2,sticky=NS)
        self._scrollbar.configure(troughcolor=settings.scrollbar['troughcolor'])
        # Bind _canvas with _scrollbar 
        self._canvas.configure(yscrollcommand=self._scrollbar.set)
        self._canvas.bind('<Configure>'
            , lambda e: self._canvas.configure(scrollregion=self._canvas.bbox("all")))
        self._frame = Frame(self._canvas)
        self._canvas.create_window((0,0),window=self._frame,anchor="nw")
        
    def _toggle(self, button:Button, jobName:str)->None:
        """
        Toggle button on/off.
        Args:
            button = tkinter Button 
            jobName = cronjob name
        """
        if self._jobs[jobName]:
            button.config(image=self._off)
            self._jobs[jobName] = False 
        else:
            button.config(image=self._on)
            self._jobs[jobName] = True 

        print(("[{0} : {1}]".format(jobName,self._jobs[jobName])))

    def _createButton(self, instantNo:int, jobName:str)->None:
        """
        Create button to on/off each cronjob.
        Args:
            instantNo = seq number of button created
            jobName = cronjob name
        """
        # Create label using cronjob command
        cronJob = ttk.Label(self._frame
                , text=jobName
                , width=75
                , anchor="w"
                , borderwidth=1
                , relief="solid")
        cronJob.grid(row=instantNo, column=0
                , ipadx=10, ipady=10
                , padx = 3, pady=3)
        cronJob.config(font=settings.app['font']
                    ,foreground=settings.cronJob['fontcolor']
                    ,background=settings.cronJob['background']
                    )
        # Set on/off button
        img = self._off
        if (self._jobs[jobName]):
            img = self._on
        # Create button
        button = ttk.Button(self._frame
                            , image=img
                            , width=50
                            , command=lambda: self._toggle(button, jobName))

        button.grid(row=instantNo, column=1
                    , ipadx=5, ipady=5
                    , padx=3 , pady=3
                    ,sticky='e')
          
    def run(self, cron:object)->None:
        """
        Run the GUI view.
        Args:
            cron : CronData object
        """
        self._jobs = cron.getJobs()
        instantNo = 0
        for jobName in self._jobs: 
            self._createButton(instantNo, jobName)
            instantNo += 1

        # Create save button    
        save = Button(self.app
                    , text ="Save"
                    , width=10
                    ,command=lambda :cron.save(self._jobs))
        save.grid(row=1
                    , ipadx=3, ipady=3
                    , padx=3 , pady=10)
        save.config(font=settings.app['font']
                    ,foreground=settings.saveButton['fontcolor']
                    ,background=settings.saveButton['background']
                    ,border=0
                    )
