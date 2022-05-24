from datetime import datetime
import pytz


class TimeProvider:

    @staticmethod
    def msk():
        return TimeProvider.__for_timezone__("Europe/Moscow")

    @staticmethod
    def __for_timezone__(name):
        tz = pytz.timezone(name)
        return datetime.now(tz)
