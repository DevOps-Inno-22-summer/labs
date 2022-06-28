import datetime
import os

class VisitsLogger:

    __file_name__ = "data/visits.txt"

    @staticmethod
    def main_page():
        os.makedirs(os.path.dirname(VisitsLogger.__file_name__), exist_ok=True)
        file = open(VisitsLogger.__file_name__, "a+")
        file.write(f"Visit at: { datetime.datetime.now() } \n")
        file.close()

    @staticmethod
    def get_visitors():
        try:
            file = open(VisitsLogger.__file_name__, "r")
            data = file.read()
            file.close()
            return data
        except IOError:
            return "No visits"
