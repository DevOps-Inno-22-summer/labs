from django.test import SimpleTestCase
from freezegun import freeze_time
from django.urls import reverse
from django.http import HttpResponse


class TestTimeView(SimpleTestCase):

    @freeze_time("2012-01-14 03:21:34")  # utc time
    def test_moscow_time_is_correct(self):

        resp: HttpResponse = self.client.get(reverse('moscow_time'))

        self.assertEqual(resp.content.decode('utf-8'), "06:21")
