from get_time import GetTime
from requests import get as requests_get
import unittest

class TestLexer(unittest.TestCase):

    def test__get_moscow_time_api__api_responds(self):
        res = requests_get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
        self.assertFalse(res.ok, "API is not responding")

    def test__api_and_local_get_time__time_diff_less_than_2s(self):
        api_time = GetTime.get_moscow_time_api()
        local_time = GetTime.get_moscow_time()

        delta = abs(api_time - local_time).total_seconds()
        self.assertLessEqual(delta, 2.0, "Timestamp difference is more than 2 seconds")

if __name__ == '__main__':
    unittest.main()
