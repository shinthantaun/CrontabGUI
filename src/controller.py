from view import View
from crondata import CronData

def runApp(testing=False)->None:
    """
    Run Crontab Manager GUI application
    
    Args:
        Testing = enable UI testing mode. Default is disable. 
    
    Exceptions:
        Raise Error: Unable to get user's crontab.
    """
    print("Opening app...\n")
    
    try:
        cron = CronData(testing)
    except:
        print("Error: Unable to get user's crontab.")
        exit()

    if(cron.isEmpty()):
        print("Empty crontab!")
        exit()

    view = View()
    view.run(cron)
    view.app.mainloop()
    print("Closed app!\n")