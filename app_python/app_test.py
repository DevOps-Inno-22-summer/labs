'''Test web application'''

import unittest
from datetime import datetime, timezone, timedelta
from app import app


class TestApp(unittest.TestCase):
    '''Testcase class'''

    def test_app(self):
        '''Test main page'''
        response = app.test_client().get('/')

        current_timezone = timezone(timedelta(hours=3))
        expected = datetime.now(current_timezone).strftime("%H:%M:%S")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(True, expected in str(response.data))
