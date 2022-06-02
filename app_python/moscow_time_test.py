import unittest
from datetime import datetime
import pytz
from moscow_time import moscow


class TestTime(unittest.TestCase):

    def test_moscow(self):
        tzone = 'Europe/Moscow'
        localDatetime = datetime.now().astimezone(pytz.timezone(tzone))
        expected = localDatetime.strftime("%Y-%m-%d %H:%M:%S")
        actual = moscow()
        self.assertEqual(expected, actual, 'Failed on moscow_test')
