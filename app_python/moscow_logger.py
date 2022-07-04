import datetime
import os

class MoscowLogger:

    __file_name__ = "data/logs.txt"

    @staticmethod
    def visitMainPage():
        os.makedirs(os.path.dirname(MoscowLogger.__file_name__), exist_ok=True)
        with open(MoscowLogger.__file_name__, "a+") as file:
            file.write(f"Visit at: { datetime.datetime.now() } \n")

    @staticmethod
    def getVisitors():
        with open(MoscowLogger.__file_name__, "r") as file:
            return file.read()