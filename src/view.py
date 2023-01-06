from tkinter import *
from tkinter import ttk
import settings

WINDOW_DM = (700,500) # (width x height)
CANVAS_WD = WINDOW_DM[0] * 0.9
CANVAS_HT = WINDOW_DM[1] * 0.8
FRAME_WD = CANVAS_WD * 0.8
FRAME_HT = CANVAS_HT * 0.7

class View:

    def __init__(self)->object:
        """Class that renders the GUI
        
        :raises Error:Cannot open images!
        """
        # Create main app
        self.app = Tk()
        self._jobs = {}
        self.app.title("Cronjob Manager")
        self.app.geometry("{0}x{1}".format(WINDOW_DM[0],WINDOW_DM[1]))
        self.app.resizable(False, False)
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

    def createCanvas(self)->Canvas:
        """Create canvas.
        
        :returns: return created tkinter Canvas
        """
        canvas = Canvas(self.app
                , bg= settings.canvas['background']
                , width=CANVAS_WD
                , height=CANVAS_HT)
        canvas.grid(column=0)
        return canvas

    def createScrollbar(self,canvas:Canvas)->Scrollbar:
        """Create scrollbar.
        
        :param Canvas canvas: tkinter canvas

        :returns: return created tkinter Scrollbar
        """
        scrollbar = Scrollbar(self.app
                    , orient='vertical'
                    , command=canvas.yview)
        scrollbar.grid(row=0,column=2,sticky=NS)
        scrollbar.configure(troughcolor=settings.scrollbar['troughcolor'])
        return scrollbar
    
    def createFrame(self,canvas:Canvas,scrollbar:Scrollbar)->Frame:
        """Bind canvas and scrollbar on the frame.
        
        :param Canvas canvas: tkinter canvas
        
        :param Scrollbar scrollbar: tkinter scrollbar

        :returns: return created tkinter Frame
        """
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>'
            , lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        frame = Frame(canvas
                , width=FRAME_WD
                , height=FRAME_HT)
        canvas.create_window((0,0),window=frame,anchor="nw")
        return frame

    def toggle(self, button:Button, jobName:str)->None:
        """Toggle button on/off.
        
        :param Button button: tkinter button
        
        :param str jobName: a particular cronjob name respective to the button
        """
        if self._jobs[jobName]:
            button.config(image=self._off)
            self._jobs[jobName] = False 
        else:
            button.config(image=self._on)
            self._jobs[jobName] = True 

        print(("[{0} : {1}]".format(jobName,self._jobs[jobName])))

    def createButton(self, instantNo:int, jobName:str, frame:Frame)->Button:
        """Create on/off button for a single cronjob.
        
        :param int instantNo: seq number of button created
        
        :param str jobName: a particular cronjob name respective to the button
        """
        # Create label using cronjob command
        cronJob = ttk.Label(frame
                , text=jobName
                , anchor="w"
                , borderwidth=1
                , relief="solid")
        cronJob.grid(row=instantNo, column=0
                , ipadx=FRAME_WD * 0.006, ipady=FRAME_HT * 0.04
                , padx = FRAME_WD * 0.06, pady=FRAME_HT * 0.02
                , sticky = NSEW)
        cronJob.config(font=('Bold', int(FRAME_WD * 0.025))
                    ,foreground=settings.cronJob['fontcolor']
                    ,background=settings.cronJob['background']
                    )
        # Set on/off button
        img = self._off
        if (self._jobs[jobName]):
            img = self._on
        # Create button
        button = ttk.Button(frame
                            , image=img
                            , command=lambda: self.toggle(button, jobName))

        button.grid(row=instantNo, column=1
                    , ipadx=FRAME_WD * 0.003, ipady=FRAME_HT * 0.01
                    , padx = FRAME_WD * 0.001, pady=FRAME_HT * 0.02
                    ,sticky=NSEW)
        return button
          
    def run(self, cron:object)->None:
        """Launch the GUI.
        
        :param object cron: CronData object
        """
        self._jobs = cron.getJobs()
        canvas = self.createCanvas()
        scrollbar = self.createScrollbar(canvas)
        frame = self.createFrame(canvas,scrollbar)

        # Create button for each job
        instantNo = 0
        for jobName in self._jobs: 
            self.createButton(instantNo, jobName,frame)
            instantNo += 1
        print("Created {0} buttons".format(instantNo))

        # Create save button    
        save = Button(self.app
                    , text ="Save"
                    ,command=lambda :cron.save(self._jobs))
        save.grid(row=1
                    , ipadx=CANVAS_WD * 0.003, ipady=CANVAS_HT * 0.003
                    , padx=CANVAS_WD * 1/3, pady=CANVAS_HT * 0.07, sticky='w')
        save.config(font=('Bold', int(FRAME_WD * 0.025))
                    ,foreground=settings.saveButton['fontcolor']
                    ,background=settings.saveButton['background']
                    ,border=2)

        # Create close button    
        create = Button(self.app
                    , text ="Close"
                    ,command=lambda : self.app.destroy())
        create.grid(row=1
                    , ipadx=CANVAS_WD * 0.003, ipady=CANVAS_HT * 0.003
                    , padx=CANVAS_WD * 1/3, pady=CANVAS_HT * 0.07, sticky='e')
        create.config(font=('Bold', int(FRAME_WD * 0.025))
                    ,foreground=settings.saveButton['fontcolor']
                    ,background=settings.saveButton['background']
                    ,border=2)
