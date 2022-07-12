from app.services.moscow_time import MoscowTime
import os


class Visits:

    def __init__(self):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        self.visitsFileName = os.path.join(fileDir, 'logs/visits.log')
        self.moscow_time = MoscowTime()

    def add_visit(self):
        time = self.moscow_time.now()
        with open(self.visitsFileName, 'a') as fp:
            fp.write(time)
            fp.write('\n')
            return time

    def get_visits(self):
        with open(self.visitsFileName, 'r') as fp:
            return fp.read().split('\n')
        


    

