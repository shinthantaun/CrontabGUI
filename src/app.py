"""Main python script to run GUI

This script is called by shell script CronjobManager.sh
"""
import controller

if __name__ == '__main__':
    #Enable testing UI mode -> true 
    controller.runApp(testing=False)
