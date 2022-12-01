import os
from crontab import CronTab
from dummycron import dummy_cronjobs

class CronData:

    def __init__(self,testing=False) -> object:
        """
        A class to get, save and refresh cronjobs.

        Args:
            Testing = enable UI testing mode. Default is disable. 
        """
        self._testing = testing
        self._user_cron = None
        if(not self._testing):
            self._user_cron = CronTab(user=os.getlogin())
        
    def isEmpty(self) -> bool:
        """
        Function to check whether there is an exisiting cronjob
        Return:
            Boolean
        """
        if(self._testing):
            return False
        if (len(self._user_cron) != 0):
            return False
        return True

    def getJobs(self) -> dict:
        """
        Get cronjob
        Return:
            Dictionary object which contains job name(key) and it's status(value)
        """
        if(self._testing):
            return dummy_cronjobs

        jobs = {}
        for eachJob in self._user_cron:
            jobs[eachJob.comment] = eachJob.is_enabled()
        return jobs


    def save(self,jobs:dict)->None:
        """
        Save the modified cronjobs. 
        Args:
            jobs = dictionary object which contains job name(key) and it's status(value)
        """
        if(self._testing):
            print("UI Testing Mode: Saved cron!")
            return

        for jobName,status in jobs.items():
            job = next(self._user_cron.find_comment(jobName))
            if job is None:
                print( "Error: not found [{0} : {1}]".format(jobName,status))
                continue    
            job.enable(status)
              
        self._user_cron.write()
        print("Saved Cronjobs!")