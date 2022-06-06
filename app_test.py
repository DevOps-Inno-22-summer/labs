'''Test web application'''

import unittest
from app import app
from datetime import datetime, timezone, timedelta


class MyTestCase(unittest.TestCase):
    '''Test class'''
    def test_app(self):
        '''Test function'''
        response = app.test_client.get('/')

        time_zone = timezone(timedelta(hours=3))
        date = datetime.now(time_zone)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(True, date in str(response.data))


if __name__ == '__main__':
    unittest.main()
