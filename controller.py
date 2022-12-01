from view import View
from crondata import CronData

def runApp()->None:
    """
    Run Crontab Manager GUI application

    Exceptions:
        Raise Error: Unable to get user's crontab.
    """
    print("Opening app...\n")
    
    try:
        cron = CronData()
    except:
        print("Error: Unable to get user's crontab.")

    if(cron.isEmpty()):
        print("Empty crontab!")
        exit()

    view = View()
    view.run(cron)
    view.app.mainloop()
    print("Closed app!\n")