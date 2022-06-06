'''Test getting current time'''

import unittest
from datetime import datetime, timezone, timedelta
from local_time import get_current_time

class TestLocalTime(unittest.TestCase):
    '''Testcase class'''

    def test_get_current_time(self):
        '''Test getting current time'''
        current_timezone = timezone(timedelta(hours=0))
        expected = datetime.now(current_timezone).strftime("%H:%M:%S")
        actual = get_current_time(0)
        self.assertEqual(expected, actual, 'Time should be equal')
