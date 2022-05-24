from time_provider import TimeProvider
from datetime import datetime
import unittest
import requests


class TestLexer(unittest.TestCase):

    def test_when_time_msk_requested_expected_answer_error_less_5s(self):
        url = "http://worldtimeapi.org/api/timezone/Europe/Moscow/"
        data = requests.get(url).json()
        expected_time = datetime.fromisoformat(data["datetime"])

        real_time = TimeProvider.msk()

        time_delta = abs(expected_time.timestamp() - real_time.timestamp())
        self.assertLessEqual(time_delta, 2.5, "Too large time error")
