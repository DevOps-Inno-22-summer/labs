from datetime import datetime
from pytz import timezone as pytz_timezone
from requests import get as requests_get

class GetTime:
    @staticmethod
    def __get_time_by_tz(tz_name):
        """Private method that returns time for specified timezone using datetime

        Args:
            tz_name (string): timezone in TZ database format (\'Continent/City\')

        Returns:
            datetime: current datetime for specified timezone
        """
        tz = pytz_timezone(tz_name)
        return datetime.now(tz)

    @staticmethod
    def get_moscow_time():
        """Method that returns Moscow time via __get_time_by_tz method

        Returns:
            datetime: current datetime for \'Europe/Moscow\' timezone
        """
        return GetTime.__get_time_by_tz("Europe/Moscow")

    @staticmethod
    def __get_time_by_tz_api(tz_name):
        """Private method that returns time for specified timezone using World Time API

        Args:
            tz_name (string): timezone in TZ database format (\'Continent/City\')

        Returns:
            datetime: datetime object containing current datetime for specified timezone
        """
        json = requests_get('http://worldtimeapi.org/api/timezone/' + tz_name).json()
        return datetime.fromisoformat(json["datetime"])

    @staticmethod
    def get_moscow_time_api():
        """Method that returns Moscow time via __get_time_by_tz_api method

        Returns:
            datetime: current datetime for \'Europe/Moscow\' timezone
        """
        return GetTime.__get_time_by_tz_api("Europe/Moscow")
