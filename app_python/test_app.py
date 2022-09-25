from time import sleep
from app import print_time
from requests import get as requests_get
from datetime import datetime
import unittest


class AppTestCase(unittest.TestCase):

    def test__api_time_properly_responds(self):
        res = requests_get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
        self.assertTrue(res.ok, "API is not responding")

    def test__api_and_app__time_diff_less_than_2s(self):

        generated_time = datetime.strptime(print_time(), "%a %b %d %H:%M:%S %Y")
        json = requests_get('http://worldtimeapi.org/api/timezone/' + "Europe/Moscow").json()
        api_given_time = datetime.fromisoformat(json["datetime"])

        delta = abs(api_given_time.replace(tzinfo=None) -  generated_time).total_seconds()
        self.assertLessEqual(delta, 2.0, "Timestamp difference is more than 2 seconds")
    
    def test_time_correctly_changed(self):
        string_time = print_time()
        sleep(2) # Sleep for 2 seconds
        string_time_two = print_time()
        delta = abs(datetime.strptime(string_time, "%a %b %d %H:%M:%S %Y") -  
        datetime.strptime(string_time_two, "%a %b %d %H:%M:%S %Y")).total_seconds()
        self.assertEqual(delta, 2, "The difference is not the same!")
        assert string_time != string_time_two

if __name__ == '__main__':
    unittest.main()