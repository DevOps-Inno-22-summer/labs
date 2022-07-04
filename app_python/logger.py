import datetime
import os

class Logger:

    __file_name__ = "data/visits.txt"

    @staticmethod
    def log_visit(path="/"):
        os.makedirs(os.path.dirname(Logger.__file_name__), exist_ok=True)
        file = open(Logger.__file_name__, "a+")
        file.write(f"[{ path }] { datetime.datetime.now() } \n")
        file.close()

    @staticmethod
    def get_visits():
        try:
            file = open(Logger.__file_name__, "r")
            data = file.read()
            file.close()
            return data.split('\n')[:-1]
        except IOError:
            return ["No visits"]
