import unittest

from datetime import datetime as dt, timezone as tz, timedelta as td
from polls.views import request_time


class TimeTestCase(unittest.TestCase):
    def test_time(self):
        time = request_time()
        self.assertEqual(time, (dt.utcnow() + td(hours=3)).strftime("%H:%M"))

if __name__ == '__main__':
    unittest.main()
