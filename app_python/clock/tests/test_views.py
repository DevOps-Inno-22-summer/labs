from django.test import TestCase
from django.urls import reverse
from clock.utills import get_current_datetime


class DateTimeViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_current_time_exists_at_response(self):
        time = get_current_datetime()
        resp = self.client.get('')
        self.assertTrue(time in resp.content.decode('utf-8'))
