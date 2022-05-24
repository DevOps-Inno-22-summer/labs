import unittest
from datetime import datetime
import pytz
from moscow_time import moscow

class TestTime(unittest.TestCase):

    def test_moscow(self):
        utcmoment_naive = datetime.utcnow()
        utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

        localFormat = "%Y-%m-%d %H:%M:%S"

        tzone = 'Europe/Moscow'
        localDatetime = utcmoment.astimezone(pytz.timezone(tzone))
        expected = localDatetime.strftime(localFormat)
        
        actual = moscow()
        self.assertEqual(expected, actual, 'Failed on moscow_test')