"""Serves as the end point to run the GUI app.
"""

from view import View
from crondata import CronData


def runApp(testing:bool=False)->None:
    """this function serves as the end point to run the GUI app.
    
    :param testing: enable UI testing mode. Default is disable, defaults to False
    :type testing: bool
    :raises Error: Unable to get user's crontab.
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
    print("\nClosed app!")
