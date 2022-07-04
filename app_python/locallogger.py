import datetime
import os

class LocalLogger:

    dirname = "data"
    logfile = "data/logs.txt"

    @staticmethod
    def addVisit():
        #may be not necessary to create folder, but just in case 
        os.makedirs(dirname, exist_ok = True)
        with open(LocalLogger.logfile, "a+") as file:
            file.write(f"New visit: { datetime.datetime.now() } \n") #server time

    @staticmethod
    def getVisits():
        with open(LocalLogger.logfile, "r") as file:
            return file.read() 