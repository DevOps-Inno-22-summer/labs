from django.test import TestCase
from django.test import Client
from unittest import mock
from datetime import datetime


class HomeTest(TestCase):

    @mock.patch('pages.views.datetime')
    def test_returned_correct_time(_, mocked_datetime):
        mocked_datetime.now.return_value = datetime(2022, 1, 1)
        c = Client()
        response = c.get('/')
        assert response.content == b"2022-01-01 00:00:00"

    def test_changed_time(_):
        c = Client()
        first_response = c.get('/')
        second_response = c.get('/')
        assert first_response != second_response
