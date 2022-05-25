from datetime import datetime
import pytz


class TimeProvider:
    """
    A static class that provide time and date for a specific region.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    msk():
        Provide current time and date in Moscow.
    """

    @staticmethod
    def msk():
        """
        Return current time and date in Moscow.

        Parameters
        ----------
        None

        Returns
        -------
        datetime:
            Current date and time in Moscow.
        """
        return TimeProvider.__for_timezone__("Europe/Moscow")

    @staticmethod
    def __for_timezone__(name):
        """
        Return current time and date for specific time zone.

        Parameters
        ----------
        name : str
            Time zone name

        Returns
        -------
        datetime:
            Current date and time in the time zone.
        """
        tz = pytz.timezone(name)
        return datetime.now(tz)
